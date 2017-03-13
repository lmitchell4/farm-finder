
""" Module summary:
Functions:
  eventShow - Show the events for a given farm.
"""

from flask import Flask, render_template, request, redirect, jsonify
from flask import url_for, flash
from flask import session as login_session

from catalog import app
from catalog.database.dbsetup import Farm, Event
from catalog.database.dbconnect import db_session

############################################################################


@app.route("/farms/<int:farm_id>/events")
def eventShow(farm_id):
  """Show the events for a given farm."""
  farm = db_session.query(Farm).filter_by(id=farm_id).one()
  events = db_session.query(Event).filter_by(farm_id=farm_id).all()
  username = login_session.get("username")

  return render_template("events.html",
                         farm=farm,
                         events=events,
                         username=username)
