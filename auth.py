from flask import Flask,redirect,render_template,Blueprint

auth = Blueprint("auth",__name__)

@auth.route('/login',['POST','GET'])
def login():
    pass
