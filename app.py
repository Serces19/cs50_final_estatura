import os
import json
from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import joinedload
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
    children = db.relationship('Child', backref='user', lazy=True)

class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.String(12), nullable=False)
    fecha_nacimiento = db.Column(db.Integer, nullable=False)
    estatura_padre = db.Column(db.Integer, nullable=False)
    estatura_madre = db.Column(db.Integer, nullable=False)
    ciudad = db.Column(db.String(30), nullable=False)
    residencia = db.Column(db.String(30), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    records = db.relationship('Record', backref='child', lazy=True)

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    height = db.Column(db.Float, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    child_id = db.Column(db.Integer, db.ForeignKey('child.id'), nullable=False)


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
    # Verificar si el usuario está autenticado
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']

    # Obtener todos los hijos del usuario
    children = Child.query.filter_by(user_id=user_id).all()
    if not children:
        return render_template('dashboard.html')

    records = db.session.query(Record, Child.name).join(Child, Record.child_id == Child.id).filter(Child.user_id == user_id).order_by(Record.month.asc()).all()
    return render_template('dashboard.html', records=records, children=children)


@app.route('/create_record', methods=['GET', 'POST'])
def create_record():
    if request.method == 'POST':
        name = request.form['name']
        height = request.form['height']
        month = request.form['month']
        child_id = Child.query.filter_by(name=name).first().id
        print('LOS DATOS SON', name, height, month, child_id)
        new_record = Record(height=height, month=month, name=name, child_id=child_id)
        db.session.add(new_record)
        db.session.commit()
        return redirect(url_for('dashboard'))
    
    user_id = session['user_id']
    children = Child.query.filter_by(user_id=user_id).all()
    return render_template('create_record.html', children=children)


@app.route('/create_child', methods=['GET', 'POST'])
def create_child():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        fecha_nacimiento = request.form['fecha_nacimiento']
        estatura_padre = request.form['estatura_padre']
        estatura_madre = request.form['estatura_madre']
        ciudad = request.form['ciudad']
        residencia = request.form['residencia']
        user_id = session['user_id']

        print(name, gender, fecha_nacimiento, estatura_padre, estatura_madre, ciudad, residencia)
        new_child = Child(name=name, user_id=user_id, gender=gender, fecha_nacimiento=fecha_nacimiento, estatura_padre=estatura_padre, estatura_madre=estatura_madre, ciudad=ciudad, residencia=residencia)
        db.session.add(new_child)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('create_child.html')


@app.route('/personas', methods=['GET', 'POST'])
def personas():
    # Verificar si el usuario está autenticado
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']

    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        fecha_nacimiento = request.form['fecha_nacimiento']
        estatura_padre = request.form['estatura_padre']
        estatura_madre = request.form['estatura_madre']
        ciudad = request.form['ciudad']
        residencia = request.form['residencia']
        user_id = session['user_id']

        print(name, gender, fecha_nacimiento, estatura_padre, estatura_madre, ciudad, residencia)
        new_child = Child(name=name, user_id=user_id, gender=gender, fecha_nacimiento=fecha_nacimiento, estatura_padre=estatura_padre, estatura_madre=estatura_madre, ciudad=ciudad, residencia=residencia)
        db.session.add(new_child)
        db.session.commit()
        return redirect(url_for('personas'))
    children = Child.query.filter_by(user_id=user_id).all()
    return render_template('personas.html', children=children)


@app.route('/charts')
def charts():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']

    # Obtener todos los hijos del usuario
    children = Child.query.filter_by(user_id=user_id).all()
    children_list = []
    for child in children:
        children_list.append(child.name)

    # Realizar una consulta combinada para obtener todos los registros del usuario con el nombre del niño
    records_with_child_name = db.session.query(Record, Child.name)\
        .join(Child, Record.child_id == Child.id)\
        .filter(Child.user_id == user_id)\
        .order_by(Record.month.asc())\
        .all()

    # Transformar los resultados a una estructura de datos serializable
    records_data = []
    for record, child_name in records_with_child_name:
        records_data.append({
            'id': record.id,
            'month': record.month,
            'height': record.height,
            'name': record.name,
            'child_name': child_name
        })

    records = json.dumps(records_data)
     
    # Datos esperados
    meses_esperado = [0, 6, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192, 204, 216, 228, 240]
    estatura_esperado = [50, 64.5, 72.7, 82, 90.3, 96.9, 103.8, 108.8, 114.9, 120.5, 125.8, 130.5, 134.5, 140, 146, 153.5, 159.5, 163.5, 166, 167, 167.5, 167.9]
    
    return render_template('charts.html', records=records, children=children_list, meses_esperado=meses_esperado, estatura_esperado=estatura_esperado)


@app.route('/delete_record/<int:record_id>', methods=['POST'])
def delete_record(record_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    current_user = session['user_id']

    record = Record.query.get_or_404(record_id)
    child_id = record.child_id
    child = Child.query.get_or_404(child_id)
    record_user_id = child.user_id
    print(f'Current user: {current_user}')
    print(f'record_user_id: {record_user_id}')
    print(type(current_user))
    print(type(record_user_id))

    if record_user_id != current_user:
        flash('No tiene permiso para realizar esta acción', 'danger')
        return redirect(url_for('dashboard'))
    
    db.session.delete(record)
    db.session.commit()
    flash('Registro eliminado correctamente', 'success')
    return redirect(url_for('dashboard'))


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