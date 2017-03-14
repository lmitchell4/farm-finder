
""" Module summary:
Functions:
  profileShow - Show the profile for a given farm.
"""

from flask import Blueprint, render_template
from flask import session as login_session

from catalog.database.dbsetup import Farm
from catalog.database.dbconnect import db_session

############################################################################

profile_show = Blueprint("profile_show", __name__)

@profile_show.route("/farms/<int:farm_id>/profile")
def profileShow(farm_id):
  """Show the profile for a given farm."""
  farm = db_session.query(Farm).filter_by(id=farm_id).one()
  username = login_session.get("username")

  return render_template("profile.html",
                          farm=farm,
                          username=username)
