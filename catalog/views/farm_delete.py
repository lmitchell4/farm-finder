
""" Module summary:
Functions:
  farmDelete - Delete an existing farm.
"""

from flask import Flask, render_template, request, redirect, jsonify
from flask import url_for, flash
from flask import session as login_session

from catalog import app
from catalog.database.dbsetup import Farm
from catalog.database.dbconnect import db_session
from catalog.views.util import imageDeleteProfile

############################################################################


@app.route("/farms/<int:farm_id>/delete", methods=["GET","POST"])
def farmDelete(farm_id):
  """Delete an existing farm."""
  farm = db_session.query(Farm).filter_by(id = farm_id).one()

  user_id = login_session.get("user_id")
  username = login_session.get("username")

  # If no one is logged in, redirect to /catalogShow:
  if not (user_id and username):
    return redirect(url_for("catalogShow",farm_id=farm_id))

  elif user_id != farm.user_id:
    return redirect(url_for("catalogShow",farm_id=farm_id))

  # Check that the login_session user_id matches the farm user_id:
  elif user_id == farm.user_id:
    if request.method == "POST":
      if farm.picture:
        imageDeleteProfile(filename=farm.picture)

      db_session.delete(farm)
      db_session.commit()
      flash("Farm Successfully Deleted: %s" % (farm.name))
      return redirect(url_for("farmsManage"))

    else:
      return render_template("farmDelete.html",
                              farm=farm,
                              username=username)
