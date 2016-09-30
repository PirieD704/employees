from flask import Flask, render_template, request, redirect, session
from flaskext.mysql import MySQL

app = Flask(__name__)
#create an instance of the mysql class
mysql = MySQL()
#add to the app (Flask object) some config data for our connection
app.config['MYSQL_DATABASE_USER'] = 'emp_user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'x'
#The name of the database we want to connect to at the DB server
app.config['MYSQL_DATABASE_DB'] = 'sakila'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
# user the mysql object's method "init_app" and pass it the flask object
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()
app.secret_key = "HAOaovn34onO3IWEFAOjskdjlEFJK2390fj756239"