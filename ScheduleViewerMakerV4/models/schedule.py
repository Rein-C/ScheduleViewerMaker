from . import db

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    subject_name = db.Column(db.String(80), nullable=False)
    class_section = db.Column(db.String(80), nullable=False)
    professor_name = db.Column(db.String(80), nullable=False)
    day_week = db.Column(db.JSON, nullable=False)
    start_time = db.Column(db.String(80), nullable=False)
    end_time = db.Column(db.String(80), nullable=False)
    room_number = db.Column(db.String(80), nullable=False)