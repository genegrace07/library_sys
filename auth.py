from flask import Flask,redirect,render_template,Blueprint,request,current_app,url_for,flash
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
        elif len(username) == 0:
            flash('Cannot be empty', 'error')
            return redirect(url_for('auth.signup'))
        else:
            flash('Sign up successfully','success')
            u_id.sign_up(username,password)
            return redirect(url_for('auth.signup'))
    else:
        return render_template('sign.html')
