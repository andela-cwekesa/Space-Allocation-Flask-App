from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/allocator'
# app.config['PGSQL_DATABASE_USER'] = 'collins'
# app.config['PGSQL_DATABASE_PASSWORD'] = 'root'
# app.config['PGSQL_DATABASE_DB'] = 'allocator'
# app.config['PGSQL_DATABASE_HOST'] = 'localhost'
db = SQLAlchemy()
db.init_app(app)
