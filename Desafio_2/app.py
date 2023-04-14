from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index_desafio():
    return render_template('index_desafio.html')
@app.route('/pagina_2')
def pagina_2():
    return render_template('pagina_2.html')
@app.route('/pagina_1')
def pagina_1():
    return render_template('pagina_1.html')