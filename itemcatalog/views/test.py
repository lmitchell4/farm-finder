
""" Module summary:
Functions:
  showIndex - Show site home.
"""

from flask import Blueprint, render_template
from flask import session as login_session

from sqlalchemy import asc

import os
from item_catalog.database.dbsetup import User

############################################################################

test = Blueprint("test", __name__)

@test.route("/")
def showIndex():
  """Show site home."""
  # return os.getcwd()
  print User
  return render_template("test.html")
