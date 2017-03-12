
""" Module summary:
Functions:
  eventEdit - Edit an event.
"""

from flask import Flask, render_template, request, redirect, jsonify
from flask import url_for, flash
from flask import session as login_session

from catalog import app
from catalog.database.dbsetup import Farm, Event
from catalog.database.dbconnect import db_session

############################################################################


@app.route("/farms/<int:farm_id>/events/<int:event_id>/edit",
            methods=["GET","POST"])
def eventEdit(farm_id, event_id):
  """Edit an event."""
  farm = db_session.query(Farm).filter_by(id=farm_id).one()
  event = db_session.query(Event).filter_by(id=event_id).one()

  user_id = login_session.get("user_id")
  username = login_session.get("username")

  if not user_id:
    return redirect(url_for("showLogin"))

  if user_id != farm.user_id:
    return redirect(url_for("errorShow"))

  if user_id == farm.user_id:
    if request.method == "POST":
      if not request.form["name"]:
        return render_template("eventEdit.html",
                               farm=farm,
                               event=event,
                               name_error=True,
                               username=username)

      event.name = request.form["name"]
      event.description = request.form["description"]

      db_session.add(event)
      db_session.commit()
      flash("Event Successfully Edited: %s" % event.name)
      return redirect(url_for("eventManage",farm_id=farm.id))

    else:
      return render_template("eventEdit.html",
                             farm=farm,
                             event=event,
                             username=username)
