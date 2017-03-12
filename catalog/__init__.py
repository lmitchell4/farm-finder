
""" Module summary:
Initialize the Flask app.
"""

from flask import Flask

############################################################################


# Initialize flask app:
app = Flask(__name__)

APPLICATION_NAME = "Farm Finder Application"

app.config['UPLOAD_FOLDER_PROFILE'] = "./catalog/static/userImages/profile"
app.config['UPLOAD_FOLDER_ITEM'] = "./catalog/static/userImages/item"
app.config['ALLOWED_EXTENSIONS'] = set(["pdf", "png", "jpg", "jpeg", "gif"])


import catalog.views.index
import catalog.views.login
import catalog.views.logout
import catalog.views.farm_show_all
import catalog.views.farm_show_user
import catalog.views.farm_edit
import catalog.views.farm_delete
import catalog.views.farm_new
import catalog.views.catalog_show
import catalog.views.catalog_manage
import catalog.views.catalog_edit
import catalog.views.catalog_delete
import catalog.views.catalog_new
import catalog.views.profile_show
import catalog.views.profile_manage
import catalog.views.profile_edit
import catalog.views.event_show
import catalog.views.event_manage
import catalog.views.event_edit
import catalog.views.event_delete
import catalog.views.event_new
import catalog.apis