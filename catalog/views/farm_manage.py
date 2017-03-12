
""" Module summary:
Functions:
  farmsManage - Show all farms belonging to the current user.
"""

from flask import Flask, render_template, request, redirect, jsonify
from flask import url_for, flash
from flask import session as login_session

from sqlalchemy import asc

from catalog import app
from catalog.database.dbsetup import Farm
from catalog.database.dbconnect import db_session

############################################################################


@app.route("/farms/manage", methods=["GET","POST"])
def farmsManage():
  """Show all farms belonging to the current user."""
  user_id = login_session.get("user_id")
  username = login_session.get("username")

  # If no one is logged in, redirct to /farm:
  if not (user_id and username):
    return redirect("/farm")

  else:
    # If someone is logged in, show them their farms:
    user_farms = db_session.query(Farm).filter_by(
                  user_id=user_id).order_by(asc(Farm.name))
    user_farms = [farm for farm in user_farms]
    return render_template("farmsManage.html",
                           user_farms=user_farms,
                           username=username)
