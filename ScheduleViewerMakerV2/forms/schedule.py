from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ScheduleForm(FlaskForm):
    subject_name = StringField('Subject Name', validators=[DataRequired()])
    class_section = StringField('Class Section', validators=[DataRequired()])
    professor_name = StringField('Professor Name', validators=[DataRequired()])
    day_week = StringField('Day/s of the Week', validators=[DataRequired()])
    time_duration = StringField('Time Duration', validators=[DataRequired()])
    room_number = StringField('Room Number', validators=[DataRequired()])
    submit = SubmitField('Add Schedule')