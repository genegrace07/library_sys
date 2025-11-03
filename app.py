from flask import  Flask,render_template,redirect,session,flash,url_for,current_app
from auth import auth
from actions import action
from librarydb import Users, Operations

app = Flask(__name__)
app.secret_key = 'mysecretkeygit '
app.config['userid'] = Users()
app.config['operate'] = Operations()

app.register_blueprint(auth,url_prefix='/')
app.register_blueprint(action,url_prefix='/')
@app.route('/libsys')
def libsys():
    user_session = session.get('username')
    if not user_session:
        flash('Invalid login, Login first', 'error')
        return redirect(url_for('auth.login'))
    else:
        user_operation = current_app.config['operate']
        view_books = user_operation.view()
        return render_template('main.html',view_books=view_books)

if __name__ == "__main__":
    app.run(debug=True)