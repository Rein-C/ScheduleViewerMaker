import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
INSTANCE_DIR = os.path.join(BASE_DIR, 'instances')

if not os.path.exists(INSTANCE_DIR):
    os.makedirs(INSTANCE_DIR)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(INSTANCE_DIR, 'schedule_viewer.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.urandom(32)