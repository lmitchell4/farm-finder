
""" Module summary:
Functions:
  eventManage - Show the events for a given farm in manage mode.
"""

from flask import Flask, render_template, request, redirect, jsonify
from flask import url_for, flash
from flask import session as login_session

from catalog import app
from catalog.database.dbsetup import Farm, Event
from catalog.database.dbconnect import db_session

############################################################################


@app.route("/farms/<int:farm_id>/events/manage")
def eventManage(farm_id):
  """Show the events for a given farm in manage mode."""
  farm = db_session.query(Farm).filter_by(id=farm_id).one()
  events = db_session.query(Event).filter_by(farm_id=farm_id).all()

  user_id = login_session.get("user_id")
  username = login_session.get("username")

  if not user_id:
    return redirect(url_for("showLogin"))

  if user_id != farm.user_id:
    return redirect(url_for("errorShow"))

  if user_id == farm.user_id:
    return render_template("eventsManage.html",
                           farm=farm,
                           events=events,
                           username=username)
