
""" Module summary:
Functions:
  editCatalogItem - Make changes to an existing catalog item.
"""

from flask import Blueprint, render_template, request, redirect
from flask import url_for, flash
from flask import session as login_session

from catalog.database.dbsetup import Farm, CatalogItem, itemCategories
from catalog.database.dbconnect import db_session
from catalog.views.util import imageUploadItem, imageDeleteItem

from util import login_required

############################################################################

catalog_edit = Blueprint("catalog_edit", __name__)

@catalog_edit.route("/farms/<int:farm_id>/catalog/<int:item_id>/edit",
                    methods=["GET","POST"])
@login_required
def editCatalogItem(farm_id, item_id):
  """Make changes to an existing catalog item."""
  farm = db_session.query(Farm).filter_by(id = farm_id).one()
  item = db_session.query(CatalogItem).filter_by(id = item_id).one()

  user_id = login_session.get("user_id")
  username = login_session.get("username")

  if user_id == item.user_id:
    if request.method == "POST":
      name = request.form.get("name")
      description = request.form.get("description")
      price = request.form.get("price")
      category = request.form.get("category")

      name_error = None
      category_error = None

      if not name:
        name_error = True
      if not category:
        category_error = True

      if name_error or category_error:
        return render_template("catalogItemEdit.html",
                               name_error=name_error,
                               category_error=category_error,
                               farm=farm,
                               item=item,
                               itemCategories=itemCategories,
                               username=username)

      item.name = request.form["name"]
      item.description = request.form["description"]
      item.price = request.form["price"]
      item.category = request.form["category"]

      f = request.form
      existing_pic = item.picture
      remove_pic = "removepicture" in f.keys() and \
                      f["removepicture"] == "no-pic"
      new_pic = request.files["picture"]

      if existing_pic:
        if remove_pic:
          imageDeleteItem(filename=item.picture)
          item.picture = None

        elif new_pic:
          imageDeleteItem(filename=item.picture)
          item.picture = imageUploadItem(farm_id=farm.id,
                                         item_id=item.id,
                                         file=new_pic)

      elif new_pic:
          item.picture = imageUploadItem(farm_id=farm.id,
                                         item_id=item.id,
                                         file=new_pic)

      db_session.add(item)
      db_session.commit()
      flash("Item Successfully Edited: %s" % (item.name))
      return redirect(url_for("catalog_manage.catalogManage", farm_id=farm_id))

    else:
      return render_template("catalogItemEdit.html",
                             farm=farm,
                             item=item,
                             itemCategories=itemCategories,
                             username=username)

  return redirect(url_for("error.errorShow"))