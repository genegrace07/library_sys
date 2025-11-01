from flask import  Flask,render_template,redirect
from auth import auth
from actions import action
from librarydb import Users

app = Flask(__name__)
app.secret_key = 'mysecretkeygit '
app.config['userid'] = Users()

app.register_blueprint(auth,url_prefix='/')
app.register_blueprint(action,url_prefix='/')
@app.route('/')
def home():
    return render_template('main.html')


if __name__ == "__main__":
    app.run(debug=True)