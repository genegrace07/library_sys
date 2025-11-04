from flask import redirect,render_template,url_for,Blueprint,request

action = Blueprint("action",__name__)

@action.route('/add',methods=['POST','GET'])
def add():
    return render_template('add.html')
    # if request.method == 'POST':
    #     request.form['']

