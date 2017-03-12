
""" Module summary:
Functions:
  farmsShowAll - Show all farms.
"""

from flask import Flask, render_template, request, redirect, jsonify
from flask import url_for, flash
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

  # If no one is logged in, show generic header and public page:
  if not (user_id and username):
    return render_template("farms.html", farms=farms)

  else:
    # If someone is logged in, show them their CRUD tabs:
    return render_template("farms.html",
                           farms=farms,
                           username=username)
