
""" Module summary:
Utility functions for accessing user data and managing user images:
  createUser - Create a new user and add them to the database.
  getUserInfo - Retrieve user object by their id.
  getUserID - Retrieve user object by their email address.
  allowedFile - Determine if the file has an allowed extension.
  imageUploadProfile - Upload a profile image.
  imageDeleteProfile - Delete a profile image.
  imageUploadItem - Upload a catalog item image.
  imageDeleteItem - Delete a catalog item image.
"""

import os
from werkzeug.utils import secure_filename

from catalog import app
from catalog.database.dbsetup import User
from catalog.database.dbconnect import db_session

############################################################################


# Helper functions for user login processes:
def createUser(login_session):
  """Create a new user and add them to the database."""
  newUser = User(name=login_session["g_username"],
                 email=login_session["email"])
  db_session.add(newUser)
  db_session.commit()
  user = db_session.query(User).filter_by(email=login_session["email"]).one()
  return user.id


def getUserInfo(user_id):
  """Retrieve user object by their id."""
  user = db_session.query(User).filter_by(id=user_id).one()
  return user


def getUserID(email):
  """Retrieve user object by their email address."""
  try:
    user = db_session.query(User).filter_by(email=email).one()
    return user.id
  except:
    return None



############################################################################


# Helper functions for managing images:
def allowedFile(filename):
  """Determine if the file has an allowed extension."""
  return "." in filename and \
         filename.rsplit(".",1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def imageUploadProfile(farm_id, file):
  """Upload a profile image."""
  if file and allowedFile(file.filename):
    filename = str(farm_id) + "_" + file.filename
    filename = secure_filename(filename)
    filedir = os.path.join(app.config['UPLOAD_FOLDER_PROFILE'], filename)

    file.save(filedir)
    return filename

  else:
    return None


def imageDeleteProfile(filename):
  """Delete a profile image."""
  os.remove(os.path.join(app.config['UPLOAD_FOLDER_PROFILE'], filename))



def imageUploadItem(farm_id, item_id, file):
  """Upload a catalog item image."""
  if file and allowedFile(file.filename):
    filename = "_".join([str(farm_id),str(item_id),file.filename])
    filename = secure_filename(filename)
    filedir = os.path.join(app.config['UPLOAD_FOLDER_ITEM'], filename)

    file.save(filedir)
    return filename

  else:
    return None


def imageDeleteItem(filename):
  """Delete a catalog item image."""
  os.remove(os.path.join(app.config['UPLOAD_FOLDER_ITEM'], filename))
