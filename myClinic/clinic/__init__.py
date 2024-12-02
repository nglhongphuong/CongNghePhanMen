from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import cloudinary
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = "HJGSHJS*&&*@#@&HSJAGDHJDHJFD"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345@localhost/myclinic?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app=app)

cloudinary.config(
       cloud_name = 'dmz9kuzue',
       api_key = '961193598266337',
       api_secret = 'yWKRKcoNtsmwsdpYhVbosl5X8Ng'
)

login = LoginManager(app=app)