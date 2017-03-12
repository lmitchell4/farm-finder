
""" Module summary:
Functions:
  catalogManage - Show the catalog for a given farm in manage mode.
"""

from flask import Flask, render_template, request, redirect, jsonify
from flask import url_for, flash
from flask import session as login_session

from catalog import app
from catalog.database.dbsetup import Farm, CatalogItem, itemCategories
from catalog.database.dbconnect import db_session

############################################################################


@app.route("/farms/<int:farm_id>/catalog/manage")
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

  if not user_id:
    return redirect(url_for("showLogin"))

  if user_id != farm.user_id:
    return redirect(url_for("errorShow"))

  if user_id == farm.user_id:
    return render_template("catalogManage.html",
                           farm=farm,
                           items=items,
                           itemCategories=itemCategories,
                           username=username)
