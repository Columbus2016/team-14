from flask import Flask, render_template, json, request, g, redirect, url_for, flash, session
from flask_mysqldb import MySQL
import MySQLdb

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'team14'
app.config['MYSQL_DB'] = 'app_etizr'
app.config['MYSQL_PORT'] = '3307'
app.config['MYSQL_HOST'] = 'localhost'
mysql.init_app(app)



@app.route("/")
def main():
	return "Welcome!";

def connect_db():
    """Connects to the specific database."""
    conn = MySQLdb.connect(host="localhost", 
                        port = 3307,
                        db="app_etizr",
                        user="root",
                        passwd="team14")
    return conn

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'MySQL'):
        g.mysql = connect_db()
    return g.mysql


@app.route('/test')
def show_test():
    cur = get_db().cursor()

    cur.execute('''SELECT max(user) FROM membership''')
    result = cur.fetchall()
    maxUser = result[0][0]

    print maxUser

    return render_template('test.html', maxUser=maxUser)

if __name__ == '__main__':
	app.run(debug=True)    