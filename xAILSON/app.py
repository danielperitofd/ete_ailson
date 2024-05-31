from flask import Flask, render_template, url_for
from conexao import get_db_connection
app = Flask(__name__)

# rota do site base;
@app.route("/")
def home():
    return render_template("site/index.html")

# rota do site ADMIN;
@app.route("/admin")
def admin():
    return render_template("admin/index.html")

# rota do site principal;
@app.route("/site")
def index():
    return render_template("site/index.html")

# rota LISTAR CATEGORIAS;
@app.route("/listar-categorias")
def listarCategoria():
    conn = get_db_connection()
    # verifica se tem e se tiver traz todos os dados da view
    categoriasview = conn.execute('SELECT * FROM categorias').fetchall()
    conn.close()
    return render_template('admin/listar-categorias.html', categorias = categoriasview)

app.run(debug=True)