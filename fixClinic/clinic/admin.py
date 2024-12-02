from clinic import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


admin = Admin(app=app, name="Private Clinic", template_mode = 'bootstrap4')
