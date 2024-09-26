from . import db

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    subject_name = db.Column(db.String(80), nullable=False)
    class_section = db.Column(db.String(80), nullable=False)
    professor_name = db.Column(db.String(80), nullable=False)
    time_duration = db.Column(db.String(80), nullable=False)