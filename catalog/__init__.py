
""" Module summary:
Initialize the Flask app.
"""

from flask import Flask

from .views.index import index
from .views.login import login
from .views.logout import logout
from .views.farm import farm
from .views.catalog import catalog
from .views.profile import profile
from .views.event import event
from .views.error import error
from .apis import apis

############################################################################


# Initialize flask app:
app = Flask(__name__)

APPLICATION_NAME = "Farm Finder Application"

app.config["UPLOAD_FOLDER_PROFILE"] = "./catalog/static/userImages/profile"
app.config["UPLOAD_FOLDER_ITEM"] = "./catalog/static/userImages/item"
app.config["ALLOWED_EXTENSIONS"] = set(["pdf", "png", "jpg", "jpeg", "gif"])

app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(logout)
app.register_blueprint(farm)
app.register_blueprint(catalog)
app.register_blueprint(profile)
app.register_blueprint(event)
app.register_blueprint(error)
app.register_blueprint(apis)
