from flask_admin.contrib.sqla import ModelView
from clinic import app, db
from flask_admin import Admin, BaseView
from clinic.models import User, UserRole
from flask_login import current_user

admin = Admin(app=app, name="Private Clinic", template_mode='bootstrap4')

class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN

class MyUserView(AuthenticatedView):
    column_list = ['id', 'name', 'username', 'email', 'user_role', 'status']
    column_searchable_list = ['username', 'name']
    column_editable_list = ['name', 'status']
    column_labels = {
        'id': 'ID',
        'name': 'Họ Tên',
        'username': 'Tên người dùng',
        'email': 'Email',
        'user_role': 'Vai trò',
        'status' : 'Trạng thái'
    }

admin.add_view(MyUserView(User, db.session))
