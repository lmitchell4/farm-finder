
""" Module summary:
Initialize the Flask app.
"""

from flask import Flask

from .views.index import index
from .views.login import login
from .views.logout import logout
from .views.farm_show_all import farm_show_all
from .views.farm_manage import farm_manage
from .views.farm_delete import farm_delete
from .views.farm_new import farm_new
from .views.catalog import catalog_show, catalog_manage, catalog_new
from .views.catalog import catalog_edit, catalog_delete
from .views.error import error
from .views.event import event_show, event_manage, event_new
from .views.event import event_delete, event_edit
from .views.profile import profile_show, profile_manage, profile_edit
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

app.register_blueprint(farm_show_all)
app.register_blueprint(farm_manage)
app.register_blueprint(farm_delete)
app.register_blueprint(farm_new)

app.register_blueprint(catalog)

app.register_blueprint(error)

app.register_blueprint(event)

app.register_blueprint(profile)

app.register_blueprint(apis)




# import catalog.views.index
# import catalog.views.login
# import catalog.views.logout
# import catalog.views.farm_show_all
# import catalog.views.farm_show_user
# import catalog.views.farm_edit
# import catalog.views.farm_delete
# import catalog.views.farm_new
# import catalog.views.catalog_show
# import catalog.views.catalog_manage
# import catalog.views.catalog_edit
# import catalog.views.catalog_delete
# import catalog.views.catalog_new
# import catalog.views.profile_show
# import catalog.views.profile_manage
# import catalog.views.profile_edit
# import catalog.views.event_show
# import catalog.views.event_manage
# import catalog.views.event_edit
# import catalog.views.event_delete
# import catalog.views.event_new
# import catalog.apis