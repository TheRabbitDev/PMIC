from flask import Flask , render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="123AsdF!@#"
app.config['MYSQL_DB']="Desafio3"

mysql = MySQL(app)

@app.route('/')
def index_desafio():
    return render_template('index_desafio.html')
@app.route('/pagina_2')
def pagina_2():
    return render_template('pagina_2.html')
@app.route('/pagina_1', methods=['GET', 'POST'])
def pagina_1():
    if request.method == 'POST':
        email = request.form['email']
        subject = request.form['subject']
        description = request.form['description']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contatos (email, assunto, descricao) VALUES (%s, %s, %s)", (email, subject, description))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('pagina_1.html')
@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    users = cur.execute("SELECT * FROM contatos")
    if users > 0:
        userData = cur.fetchall()
    else:
        userData = []
    return render_template("users.html", userData=userData)

