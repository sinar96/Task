""" Configuration File """
import os

# Development (Debug -> True)
DEBUG = True
PROJECT_DIR = os.path.dirname(os.path.abspath(__name__))

#SQLITE
SQLALCHEMY_DATABASE_URI = 'mysql://root:sinar123@localhost/task'
