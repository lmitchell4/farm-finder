
""" Module summary:
Functions:
  newFarm - Create a new farm and add it to the database.
"""

from flask import Flask, render_template, request, redirect, jsonify
from flask import url_for, flash
from flask import session as login_session

from catalog import app
from catalog.database.dbsetup import Farm
from catalog.database.dbconnect import db_session
from catalog.views.util import imageUploadProfile

from util import login_required

############################################################################


@app.route("/farms/new", methods=["GET","POST"])
@login_required
def newFarm():
  """Create a new farm and add it to the database."""
  user_id = login_session.get("user_id")
  username = login_session.get("username")
 
  # Check that the user_id argument matches the login_session user_id.
  if request.method == "POST":
    if not request.form["name"]:
      return render_template("farmNew.html",
                             name_error=True,
                             username=username)

    newFarm = Farm(name = request.form["name"],
                   location = request.form["location"],
                   description = request.form["description"],
                   picture = None,
                   user_id=login_session["user_id"])
    db_session.add(newFarm)
    db_session.commit()

    picture = request.files["picture"]
    if picture:
      db_session.refresh(newFarm)
      picture_name = imageUploadProfile(farm_id=newFarm.id, file=picture)
      newFarm.picture = picture_name
      db_session.add(newFarm)
      db_session.commit()

    flash("New Farm %s Successfully Created" % newFarm.name)
    return redirect(url_for("farmsManage"))

  else:
    return render_template("farmNew.html",
                           username=username)

  return render_template("farmNew.html",
                         error=request.files["picture"])
