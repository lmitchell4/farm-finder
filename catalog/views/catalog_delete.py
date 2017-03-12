
""" Module summary:
Functions:
  deleteCatalogItem - Delete an existing catalog item.
"""

from flask import Flask, render_template, request, redirect, jsonify
from flask import url_for, flash
from flask import session as login_session

from catalog import app
from catalog.database.dbsetup import Farm, CatalogItem
from catalog.database.dbconnect import db_session
from catalog.views.util import imageDeleteItem

############################################################################


@app.route("/farms/<int:farm_id>/catalog/<int:item_id>/delete",
            methods=["GET","POST"])
def deleteCatalogItem(farm_id, item_id):
  """Delete an existing catalog item."""
  farm = db_session.query(Farm).filter_by(id = farm_id).one()
  item = db_session.query(CatalogItem).filter_by(id = item_id).one()

  user_id = login_session.get("user_id")
  username = login_session.get("username")

  if not user_id:
    return redirect(url_for("showLogin"))

  if user_id != item.user_id:
    return redirect(url_for("errorShow"))

  if user_id == item.user_id:
    if request.method == "POST":
      db_session.delete(item)
      db_session.commit()

      if item.picture:
        imageDeleteItem(filename=item.picture)

      flash("Item Successfully Deleted: %s" % (item.name))
      return redirect(url_for("catalogManage", farm_id=farm_id))

    else:
      return render_template("catalogItemDelete.html",
                             farm=farm,
                             item=item,
                             username=username)
