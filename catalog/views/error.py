
""" Module summary:
Functions:
  errorShow - Page for when there is an error.
"""

from flask import render_template
from flask import session as login_session

from catalog import app

############################################################################


@app.route("/error")
def errorShow():
  """Page for when there is an error."""
  username = login_session.get("username")

  return render_template("error.html", username=username)
