
""" Module summary:
Functions:
  eventDelete - Delete an event.
"""

from flask import Flask, render_template, request, redirect, jsonify
from flask import url_for, flash
from flask import session as login_session

from catalog import app
from catalog.database.dbsetup import Farm, Event
from catalog.database.dbconnect import db_session

from util import login_required

############################################################################


@app.route("/farms/<int:farm_id>/events/<int:event_id>/delete",
            methods=["GET","POST"])
@login_required
def eventDelete(farm_id, event_id):
  """Delete an event."""
  farm = db_session.query(Farm).filter_by(id=farm_id).one()
  event = db_session.query(Event).filter_by(id=event_id).one()

  user_id = login_session.get("user_id")
  username = login_session.get("username")

  if user_id == farm.user_id:
    if request.method == "POST":
      db_session.delete(event)
      db_session.commit()

      flash("Event Successfully Deleted: %s" % (event.name))
      return redirect(url_for("eventManage",farm_id=farm.id))

    else:
      return render_template("eventDelete.html",
                             farm=farm,
                             event=event,
                             username=username)

  else:
    return redirect(url_for("errorShow"))
