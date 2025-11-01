from flask import Flask,redirect,render_template,Blueprint,request,current_app,url_for,flash
from werkzeug.security import generate_password_hash,check_password_hash
import librarydb

auth = Blueprint("auth",__name__)

@auth.route('/signup',methods=['POST','GET'])
def signup():
    u_id = current_app.config['userid']
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        existing = u_id.get_username(username)
        if existing:
            flash(f'{username} already exist','error')
            return redirect(url_for('auth.signup'))
        elif len(username) == 0 or len(password) == 0:
            flash('Username and Password cannot be empty', 'error')
            return redirect(url_for('auth.signup'))
        else:
            flash('Sign up successfully','success')
            password_hashed = generate_password_hash(password)
            u_id.sign_up(username,password_hashed)
            return redirect(url_for('auth.signup'))
    else:
        return render_template('sign.html')
