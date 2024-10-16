from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .schedule import Schedule

__all__ = ['User', 'Schedule', 'db']