from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#database object
db = SQLAlchemy()

def create_app():
    app = Flask(__name__,template_folder = 'templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:arunrockstar@localhost/aws_project'
    db.init_app(app)

    #import later open
    from routes import register_routes
    register_routes(app,db)

    migrate = Migrate(app,db)
    return app