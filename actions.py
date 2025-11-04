from flask import redirect,render_template,url_for,Blueprint,request

action = Blueprint("action",__name__)

@action.route('/available',methods=['POST','GET'])
def available():
    pass
    # if request.method == 'POST':
    #     request.form['']

