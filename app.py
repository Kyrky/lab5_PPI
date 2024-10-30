from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    steps = db.Column(db.Text, nullable=True)
    expected_result = db.Column(db.Text, nullable=True)
    actual_result = db.Column(db.Text, nullable=True)
    priority = db.Column(db.String(10), nullable=True)
    assigned = db.Column(db.String(20), nullable=True)
    status = db.Column(db.String(20), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Account created!", "success")
        return redirect(url_for('login'))
    return render_template("register.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash("Logged in successfully!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Login failed. Check email and password.", "danger")
    return render_template("login.html")

@app.route("/dashboard")
@login_required
def dashboard():
    reports = Report.query.filter_by(user_id=current_user.id).all()
    return render_template("dashboard.html", reports=reports)

@app.route("/report/new", methods=['GET', 'POST'])
@login_required
def new_report():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        steps = request.form.get('steps')
        expected_result = request.form.get('expected_result')
        actual_result = request.form.get('actual_result')
        priority = request.form.get('priority')
        assigned = request.form.get('assigned')
        status = request.form.get('status')
        
        report = Report(
            title=title,
            description=description,
            steps=steps,
            expected_result=expected_result,
            actual_result=actual_result,
            priority=priority,
            assigned=assigned,
            status=status,
            user_id=current_user.id
        )
        db.session.add(report)
        db.session.commit()
        flash("Report created!", "success")
        return redirect(url_for('dashboard'))
    return render_template("new_report.html")

@app.route("/report/<int:report_id>")
@login_required
def view_report(report_id):
    report = Report.query.get_or_404(report_id)
    return render_template("view_report.html", report=report)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
