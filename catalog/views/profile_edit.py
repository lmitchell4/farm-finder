
""" Module summary:
Functions:
  profileEdit - Edit the profile for a given farm.
"""

from flask import Flask, render_template, request, redirect, jsonify
from flask import url_for, flash
from flask import session as login_session

from catalog import app
from catalog.database.dbsetup import Farm
from catalog.database.dbconnect import db_session
from catalog.views.util import imageUploadProfile, imageDeleteProfile

from util import login_required

############################################################################


@app.route("/farms/<int:farm_id>/profile/edit", methods=["GET","POST"])
@login_required
def profileEdit(farm_id):
  """Edit the profile for a given farm."""
  farm = db_session.query(Farm).filter_by(id=farm_id).one()

  user_id = login_session.get("user_id")
  username = login_session.get("username")

  if user_id != farm.user_id:
    return redirect(url_for("errorShow"))

  if user_id == farm.user_id:
    if request.method == "POST":
      if not request.form["name"]:
        return render_template("profileEdit.html",
                               farm=farm,
                               name_error=True,
                               username=username)

      farm.name = request.form["name"]
      farm.location = request.form["location"]
      farm.description = request.form["description"]

      f = request.form
      existing_pic = farm.picture
      remove_pic = "removepicture" in f.keys() and \
                      f["removepicture"] == "no-pic"
      new_pic = request.files["picture"]

      if existing_pic:
        if remove_pic:
          imageDeleteProfile(filename=farm.picture)
          farm.picture = None

        elif new_pic:
          imageDeleteProfile(filename=farm.picture)
          farm.picture = imageUploadProfile(farm_id=farm.id, file=new_pic)

      elif new_pic:
          farm.picture = imageUploadProfile(farm_id=farm.id, file=new_pic)

      db_session.add(farm)
      db_session.commit()
      flash("Profile Successfully Edited")
      return redirect(url_for("profileManage", farm_id=farm_id))

    else:
      return render_template("profileEdit.html",
                             farm=farm,
                             username=username)
