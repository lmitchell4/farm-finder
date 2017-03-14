
""" Module summary:
Functions:
  eventNew - Create a new event.
"""

from flask import Blueprint, render_template, request, redirect, url_for
from flask import flash
from flask import session as login_session

# from catalog import app
from catalog.database.dbsetup import Farm, Event
from catalog.database.dbconnect import db_session

from util import login_required

############################################################################

event_new = Blueprint("event_new", __name__)

@event_new.route("/farms/<int:farm_id>/events/new", methods=["GET","POST"])
@login_required
def eventNew(farm_id):
  """Create a new event."""
  farm = db_session.query(Farm).filter_by(id=farm_id).one()

  user_id = login_session.get("user_id")
  username = login_session.get("username")

  if user_id == farm.user_id:
    if request.method == "POST":
      if not request.form["name"]:
        return render_template("eventNew.html",
                               farm=farm,
                               name_error=True,
                               username=username)

      event = Event(name = request.form["name"],
                     description = request.form["description"],
                     farm_id=farm.id,
                     user_id=user_id)

      db_session.add(event)
      flash("New Event Successfully Created: %s" % event.name)
      db_session.commit()
      return redirect(url_for("event_manage.eventManage",farm_id=farm.id))

    else:
      return render_template("eventNew.html",
                             farm=farm,
                             username=username)

  else:
    return redirect(url_for("error.errorShow"))
