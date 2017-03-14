
""" Module summary:
Functions:
  farmsShowAll - Show all farms.
"""

from flask import render_template
from flask import session as login_session

from sqlalchemy import asc

from catalog import app
from catalog.database.dbsetup import Farm
from catalog.database.dbconnect import db_session

############################################################################


@app.route("/farms")
def farmsShowAll():
  """Show all farms."""
  farms = db_session.query(Farm).order_by(asc(Farm.name))

  user_id = login_session.get("user_id")
  username = login_session.get("username")

  return render_template("farms.html",
                         farms=farms,
                         username=username)
