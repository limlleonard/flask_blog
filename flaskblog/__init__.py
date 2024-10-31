from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret' #'5791628bb0b13ce0c676dfde280ba245'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# this will create a instance folder and place .db there
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../flaskblog/site.db'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://uwqvstqhzwieuecz7zwg:RJXe2Ge80Sw5rehSPrHHDHFn6FGyMF@bvusyauiyibht5nvqff6-postgresql.services.clever-cloud.com:50013/bvusyauiyibht5nvqff6'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes
