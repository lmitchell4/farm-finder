
""" Module summary:
Functions:
  profileManage - Show the profile for a given farm in manage mode.
"""

from flask import Flask, render_template, request, redirect, jsonify
from flask import url_for, flash
from flask import session as login_session

from catalog import app
from catalog.database.dbsetup import Farm
from catalog.database.dbconnect import db_session

############################################################################


@app.route("/farms/<int:farm_id>/profile/manage")
def profileManage(farm_id):
  """Show the profile for a given farm in manage mode."""
  farm = db_session.query(Farm).filter_by(id=farm_id).one()

  user_id = login_session.get("user_id")
  username = login_session.get("username")

  # If no one is logged in, show generic header and public page:
  if not user_id:
    return redirect(url_for("showLogin"))

  if user_id != farm.user_id:
    return redirect(url_for("errorShow"))

  if user_id == farm.user_id:
    return render_template("profileManage.html",
                           farm=farm,
                           username=username)
