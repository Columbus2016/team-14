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

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        cur = get_db().cursor()
        cur.execute('''SELECT password from users where email = %s''',request.form['username'])
        if request.form['password'] != cur.fetchall()[0]:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(main_page)
    return render_template('login.html', error=error)



class User:
    def __init__(self, id, firstName, lastName, email, birthday, location, gender, points, groupID):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.birthday = birthday
        self.location = location
        self.gender = gender
        self.points = points
        self.groupID = groupID

    def validatePurchase(self, product):
        self.points += product.points

    def joinGroup(self, groupID):
        self.groupID = groupID

class Group:
    def __init__(self, id, name, creator, points, description):
        self.id = id
        self.name = name
        self.creator = creator
        self.points = points
        self.description = description

class Product:
    def __init__(self, product, points):
        self.product = product
        self.points = points

class Competition:
    def __init__(self, id, group1, group2, inSession):
        self.id = id
        self.group1 = group1
        self.group2 = group2
        self.points1 = 0
        self.points2 = 0
        self.inSession = inSession

    def addToGroupOne(self, points):
        if self.inSession:
            self.points1 += points

    def addToGroupTwo(self, points):
        if self.inSession:
            self.points2 += points

    def endCompetition(self):
        self.inSession = False
class Quiz:
    def _init_(self, possiblePoints,pointGain, user):
        self.possiblePoints = possiblePoints
        self.pointGain = pointGain
        self.user = user
