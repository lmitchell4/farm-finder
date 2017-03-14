
""" Module summary:
Functions:
  catalogShow - Show the catalog for a given farm."
"""

from flask import render_template
from flask import session as login_session

from catalog import app
from catalog.database.dbsetup import Farm, CatalogItem, itemCategories
from catalog.database.dbconnect import db_session

############################################################################


@app.route("/farms/<int:farm_id>")
@app.route("/farms/<int:farm_id>/catalog")
def catalogShow(farm_id):
  """Show the catalog for a given farm."""
  farm = db_session.query(Farm).filter_by(id=farm_id).one()
  username = login_session.get("username")
  items_list = db_session.query(CatalogItem).filter_by(farm_id=farm_id).all()

  items = {}
  for item in items_list:
    if items.has_key(item.category):
      items[item.category].append(item)
    else:
      items[item.category] = [item]

  return render_template("catalog.html",
                         farm=farm,
                         items=items,
                         itemCategories=itemCategories,
                         username=username)
