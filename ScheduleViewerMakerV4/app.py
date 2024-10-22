from flask import Flask, render_template, request, redirect, url_for, flash, abort, send_file
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import LoginForm, SignupForm, ScheduleForm
from models import db, User, Schedule
from weasyprint import HTML
from io import BytesIO
import os

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('schedule'))
        else:
            flash('Invalid username or password')
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully!')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/schedule', methods=['GET', 'POST'])
@login_required
def schedule():
    form = ScheduleForm()
    if form.validate_on_submit():
        new_schedule = Schedule(
            user_id=current_user.id,
            subject_name=form.subject_name.data,
            class_section=form.class_section.data,
            professor_name=form.professor_name.data,
            day_week=form.day_week.data, 
            start_time=form.start_time.data,
            end_time=form.end_time.data,
            room_number=form.room_number.data
        )
        db.session.add(new_schedule)
        db.session.commit()
        flash('Schedule added successfully!')
    schedules = Schedule.query.filter_by(user_id=current_user.id).all()
    return render_template('schedule.html', form=form, schedules=schedules)

@app.route('/schedule/delete/<int:schedule_id>', methods=['POST'])
@login_required
def delete_schedule(schedule_id):
    schedule = Schedule.query.get_or_404(schedule_id)
    if schedule.user_id != current_user.id:
        abort(403)
    db.session.delete(schedule)
    db.session.commit()
    flash('Schedule deleted successfully!')
    return redirect(url_for('schedule'))

@app.route('/export/pdf')
@login_required
def export_pdf():
    schedules = Schedule.query.filter_by(user_id=current_user.id).all()
    html = render_template('schedule_pdf.html', schedules=schedules)
    pdf = HTML(string=html).write_pdf()
    return send_file(BytesIO(pdf), as_attachment=True, download_name='schedule.pdf')

if __name__ == '__main__':
    app.run(debug=True)