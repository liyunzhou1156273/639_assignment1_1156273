
import mysql.connector, MySQLdb.cursors, git, os, smtplib, db.query as query,bcrypt

from flask import Flask, render_template, request, redirect, url_for, session, flash
from db import db,query

#from features.staff.staff import staff
#from features.student.student import student
#from features.mentor.mentor import mentor
from common.user import *
from ci import ci
from dotenv import load_dotenv
#from common.login_required import student_login_required
from itsdangerous import URLSafeTimedSerializer
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = "I'm a secret unique key"

# app.config['MYSQL_HOST']='localhost'
# app.config['MYSQL_USER']='root'
# app.config['MYSQL_PASSWORD']='1234'

@app.route("/")
def home():
    return render_template("login.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.clear()
        return render_template("login.html")
    
    email = request.form['email'].strip()
    password = request.form['password'].strip()
    params=["email"]

 




    # if user and bcrypt.check_password_hash(user['password'], password):
    #         flash('Login successful!', 'success')
    #         return redirect(url_for('home'))
    #     else:
    #         flash('Login failed. Check your username and password.', 'danger')

    # return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        user = {
            'username': username,
            'password': hashed_password
        }

        users.append(user)

        flash('Registration successful! You can now login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')