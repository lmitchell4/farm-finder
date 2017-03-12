
""" Module summary:
Functions:
  showIndex - Show site home.
"""

from flask import Flask, render_template, request, redirect, jsonify
from flask import session as login_session

from sqlalchemy import asc

from catalog import app

############################################################################


@app.route("/")
def showIndex():
  """Show site home."""
  user_id = login_session.get("user_id")
  username = login_session.get("username")

  if not (user_id and username):
    return render_template("index.html")

  else:
    return render_template("index.html",
                           username=username)
