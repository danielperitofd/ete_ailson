from flask import Flask, render_template, url_for
from conexao import get_db_connection
app = Flask(__name__)

# rota do site base;

@app.route("/")
def index():
    return render_template("site/index.html")
# rota do site principal;
# o que colocar de nome após o app.route, coloque também após def.
@app.route("/home")
def home():
    return render_template("site/index.html")

# rota do site ADMIN;
@app.route("/about")
def about():
    return render_template("site/about.html")



# rota LISTAR noticias;
@app.route("/list-news")
def listNews():
    conn = get_db_connection()
    # verifica se tem e se tiver traz todos os dados da view
    news_view = conn.execute('SELECT * FROM news').fetchall()
    conn.close()
    return render_template('admin/list-news.html', news = news_view)

app.run(debug=True)