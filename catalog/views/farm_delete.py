
""" Module summary:
Functions:
  farmDelete - Delete an existing farm.
"""

from flask import render_template, request, redirect, url_for, flash
from flask import session as login_session

from catalog import app
from catalog.database.dbsetup import Farm
from catalog.database.dbconnect import db_session
from catalog.views.util import imageDeleteProfile

from util import login_required

############################################################################


@app.route("/farms/<int:farm_id>/delete", methods=["GET","POST"])
@login_required
def farmDelete(farm_id):
  """Delete an existing farm."""
  farm = db_session.query(Farm).filter_by(id = farm_id).one()

  user_id = login_session.get("user_id")
  username = login_session.get("username")

  # Check that the login_session user_id matches the farm user_id:
  if user_id == farm.user_id:
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

  else:
    return redirect(url_for("catalogShow",farm_id=farm_id))
