from flask import redirect,render_template,url_for,Blueprint,request,current_app,flash

action = Blueprint("action",__name__)

@action.route('/add',methods=['POST','GET'])
def add():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        user_op = current_app.config['useroperate']
        add_book = user_op.add_books(title,author)
        flash(f'{title} successfully added')
        return render_template('add.html')
    else:
        return render_template('add.html')


