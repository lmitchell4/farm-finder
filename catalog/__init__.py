
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
from .views.catalog_show import catalog_show
from .views.catalog_manage import catalog_manage
from .views.catalog_edit import catalog_edit
from .views.catalog_delete import catalog_delete
from .views.catalog_new import catalog_new
from .views.event_show import event_show
from .views.event_manage import event_manage
from .views.event_edit import event_edit
from .views.event_delete import event_delete
from .views.event_new import event_new
from .views.profile_show import profile_show
from .views.profile_manage import profile_manage
from .views.profile_edit import profile_edit
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

app.register_blueprint(catalog_show)
app.register_blueprint(catalog_manage)
app.register_blueprint(catalog_edit)
app.register_blueprint(catalog_delete)
app.register_blueprint(catalog_new)

app.register_blueprint(event_show)
app.register_blueprint(event_manage)
app.register_blueprint(event_edit)
app.register_blueprint(event_delete)
app.register_blueprint(event_new)

app.register_blueprint(profile_show)
app.register_blueprint(profile_manage)
app.register_blueprint(profile_edit)

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