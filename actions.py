from flask import redirect,render_template,url_for,Blueprint,request,current_app,flash

action = Blueprint("action",__name__)

@action.route('/add',methods=['POST','GET'])
def add():
    if_empty = {None:'Unknown'}
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author') or if_empty[None]
        user_op = current_app.config['useroperate']

        if title:
            add_book = user_op.add_books(title,author)
            flash(f'{title} successfully added','success')
            return render_template('add.html')
        else:
            flash('Title cannot be empty','error')
            return redirect(url_for('action.add'))
    else:
        return render_template('add.html')
@action.route('/actionhandling/<int:book_id>',methods=['POST','GET'])
def action_handling(book_id):
        useractions = current_app.get['useraction']
        if 'update' in request.form:
            return render_template('update.html',book_id=book_id)
        elif 'delete' in request.form:
            return render_template('delet.html',book_id=book_id)


