from clinic import app, utils, login
from flask_login import login_user, logout_user
from flask import render_template, request, url_for, redirect
import cloudinary.uploader
from clinic.models import UserRole, Gender

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/register', methods=['get','post'])
def user_register():
    err_msg = ""

    if request.method.__eq__('POST'):
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        confirm = request.form.get('confirm')
        dob = request.form.get('dob')
        phone = request.form.get('phone')
        avatar_path = None
        gender = None
        if request.form.get('gender') == 'male':
            gender = Gender.MALE
        else:
            gender = Gender.FEMALE
        try:
            if password.strip().__eq__(confirm.strip()):
                avatar = request.files.get('avatar')
                if avatar:
                  res = cloudinary.uploader.upload(avatar)
                  avatar_path = res['secure_url']
               #kiểm tra mật khẩu xác thực
                utils.add_user(name=name, username=username,
                           password=password,email=email, avatar=avatar_path, gender=gender, dob=dob, phone=phone)
                return redirect(url_for('user_login'))
            else:
                err_msg = "Mật khẩu không khớp !!"
        except Exception as ex:
            err_msg="Hệ thống đang lỗi" + str(ex)

    return render_template("auth/register.html", err_msg=err_msg)

@app.route('/login', methods=['get', 'post'])
def user_login():
    err_msg = ""
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        user = utils.check_login(username=username, password=password)
        if user:
            #Ghi nhan trang thai dang nhap user qua flask_login import login_user
            login_user(user=user)
            return redirect(url_for('index'))
        else:
            err_msg = "Username or Password is not exactly!!"

    return render_template("auth/login.html", err_msg=err_msg)


@app.route('/admin-login', methods=['post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = utils.check_login(username=username,
                                 password=password,
                                 role=UserRole.ADMIN)
    if user:
    #Ghi nhan trang thai dang nhap user qua flask_login import login_user
        login_user(user=user)
    return redirect('/admin')


@login.user_loader
def user_load(user_id):
    return utils.get_user_by_id(user_id)


@app.route('/signout', methods=['get', 'post'])
def user_signout():
    logout_user()
    return redirect(url_for('user_login'))


if __name__ == "__main__":
    #nạp trang admin
    from clinic.admin import *
    app.run(debug=True)