import os
from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


###############################################################################################################

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    records = db.relationship('Record', backref='user', lazy=True)


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Float, nullable=False)
    date = db.Column(db.String(10), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

##################################################################################################################


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Check your email and password.')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    records = Record.query.filter_by(user_id=user_id).all()
    return render_template('dashboard.html', records=records)


@app.route('/create_record', methods=['GET', 'POST'])
def create_record():
    if request.method == 'POST':
        height = request.form['height']
        date = request.form['date']
        user_id = session['user_id']
        new_record = Record(height=height, date=date, user_id=user_id)
        db.session.add(new_record)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('create_record.html')


@app.route('/charts')
def charts():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    records = Record.query.filter_by(user_id=user_id).all()
    return render_template('charts.html', records=records)


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.')
    return redirect(url_for('home'))


@app.route('/init_db')
def init_db():
    with app.app_context():
        db.create_all()
        return "Database initialized!"


if __name__ == '__main__':
    app.run(debug=True)