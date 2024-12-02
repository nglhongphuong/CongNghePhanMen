from clinic.dao import hash_password, auth_password
from clinic import app, db
from clinic.models import User, UserRole

def add_user(name, username, password, **kwargs):
    password = hash_password(password)
    user = User(name=name.strip(), username=username.strip(),
                password=password,
                email=kwargs.get('email'),
                avatar=kwargs.get('avatar'))

    db.session.add(user)
    db.session.commit()

def check_login(username, password, role=UserRole.PATIENT):
    #Truy xuất nguyên đối tượng dựa trên
    user = User.query.filter_by(username=username.strip()).first()
    if user and auth_password(password, user.password):
        return user
    return None

def get_user_by_id(user_id):
    return User.query.get(user_id)

