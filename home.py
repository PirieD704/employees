#pip install flask-cors must be done in the terminal when the server is not running in the virtualenv
from flask import Flask, render_template, request, redirect, session, jsonify
from flaskext.mysql import MySQL
from flask_cors import CORS

app = Flask(__name__)
#create an instance of the mysql class
mysql = MySQL()
#add to the app (Flask object) some config data for our connection
CORS(app)
app.config['MYSQL_DATABASE_USER'] = 'emp_user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'x'
#The name of the database we want to connect to at the DB server
app.config['MYSQL_DATABASE_DB'] = 'sakila'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
# user the mysql object's method "init_app" and pass it the flask object
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()
app.secret_key = "HAOEA2342352LKT3wlekfjaow23n2039jqj23r48t02h2alkg30aapo32j"

# @app.route('/')
# def index():
# 	return render_template('index.html')

@app.route('/customers')
def customers():
	query = "SELECT name, address, city, `zip code`, sum(payment.amount) as total, staff.username as total FROM customer_list LEFT JOIN payment ON customer_list.id = payment.customer_id LEFT JOIN staff ON customer_list.SID = staff.staff_id LEFT JOIN store ON staff.store_id = store.store_id WHERE SID = 1 GROUP BY name, address, city, `zip code`, staff.username"
	cursor.execute(query)
	data = cursor.fetchall()
	data_as_list = list(data)
	return jsonify(results = data_as_list)
	# return render_template('customers.html',
		# data = data)

@app.route('/customers_view')
def customers_view():
	return render_template('customers.html')

if __name__ == "__main__":
	app.run(debug=True)