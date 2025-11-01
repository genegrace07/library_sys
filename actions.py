from flask import redirect,render_template,url_for,Blueprint

action = Blueprint("action",__name__)

@action.route('/login',methods=['POST','GET'])
def login():
    return render_template('login.html')