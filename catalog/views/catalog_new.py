
""" Module summary:
Functions:
  newItem - Create a new catalog item and add it to the database.
"""

from flask import Flask, render_template, request, redirect, jsonify
from flask import url_for, flash
from flask import session as login_session

from catalog import app
from catalog.database.dbsetup import Farm, CatalogItem, itemCategories
from catalog.database.dbconnect import db_session
from catalog.views.util import imageUploadItem

from util import login_required

############################################################################


@app.route("/farms/<int:farm_id>/catalog/new", methods=["GET","POST"])
@login_required
def newItem(farm_id):
  """Create a new catalog item and add it to the database."""
  farm = db_session.query(Farm).filter_by(id = farm_id).one()

  user_id = login_session.get("user_id")
  username = login_session.get("username")

  if user_id == farm.user_id:
    if request.method == "POST":
      newItem = CatalogItem(name=request.form["name"],
                            description=request.form["description"],
                            price=request.form["price"],
                            category=request.form["category"],
                            farm_id=farm_id,
                            user_id=farm.user_id,
                            picture=None)
      db_session.add(newItem)
      db_session.commit()

      picture = request.files["picture"]
      if picture:
        db_session.refresh(newItem)
        picture_name = imageUploadItem(farm_id=farm.id,
                                        item_id=newItem.id,
                                        file=picture)
        newItem.picture = picture_name
        db_session.add(newItem)
        db_session.commit()

      flash("New Item Successfully Created: %s" % (newItem.name))
      return redirect(url_for("catalogManage", farm_id=farm_id))

    else:
      return render_template("catalogItemNew.html",
                             farm=farm,
                             itemCategories=itemCategories,
                             username=username)

  else:
    return redirect(url_for("errorShow"))
