
""" Module summary:
Functions:
  catalogManage - Show the catalog for a given farm in manage mode.
"""

from flask import Blueprint, render_template, redirect, url_for
from flask import session as login_session

# from catalog import app
from catalog.database.dbsetup import Farm, CatalogItem, itemCategories
from catalog.database.dbconnect import db_session

from util import login_required

############################################################################

catalog_manage = Blueprint("catalog_manage", __name__)

@catalog_manage.route("/farms/<int:farm_id>/catalog/manage")
@login_required
def catalogManage(farm_id):
  """Show the catalog for a given farm in manage mode."""
  farm = db_session.query(Farm).filter_by(id=farm_id).one()
  items_list = db_session.query(CatalogItem).filter_by(farm_id = farm_id).all()
  items = {}
  for item in items_list:
    if items.has_key(item.category):
      items[item.category].append(item)
    else:
      items[item.category] = [item]

  user_id = login_session.get("user_id")
  username = login_session.get("username")

  if user_id == farm.user_id:
    return render_template("catalogManage.html",
                           farm=farm,
                           items=items,
                           itemCategories=itemCategories,
                           username=username)

  else:
    return redirect(url_for("error.errorShow"))