
""" Module summary:
Functions:
  profileManage - Show the profile for a given farm in manage mode.
"""

from flask import Blueprint, render_template, redirect, url_for
from flask import session as login_session

# from catalog import app
from catalog.database.dbsetup import Farm
from catalog.database.dbconnect import db_session

from util import login_required

############################################################################

profile_manage = Blueprint("profile_manage", __name__)

@profile_manage.route("/farms/<int:farm_id>/profile/manage")
@login_required
def profileManage(farm_id):
  """Show the profile for a given farm in manage mode."""
  farm = db_session.query(Farm).filter_by(id=farm_id).one()

  user_id = login_session.get("user_id")
  username = login_session.get("username")

  if user_id != farm.user_id:
    return redirect(url_for("error.errorShow"))

  if user_id == farm.user_id:
    return render_template("profileManage.html",
                           farm=farm,
                           username=username)
