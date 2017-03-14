
""" Module summary:
Functions:
  farmsManage - Show all farms belonging to the current user.
"""

from flask import Blueprint, render_template
from flask import session as login_session

from sqlalchemy import asc

from catalog.database.dbsetup import Farm
from catalog.database.dbconnect import db_session

from util import login_required

############################################################################

farm_manage = Blueprint("farm_manage", __name__)

@farm_manage.route("/farms/manage", methods=["GET","POST"])
@login_required
def farmsManage():
  """Show all farms belonging to the current user."""
  user_id = login_session.get("user_id")
  username = login_session.get("username")
  
  # If someone is logged in, show them their farms:
  user_farms = db_session.query(Farm).filter_by(
                user_id=user_id).order_by(asc(Farm.name))
  user_farms = [farm for farm in user_farms]
  return render_template("farmsManage.html",
                         user_farms=user_farms,
                         username=username)
