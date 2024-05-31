# Sessão importação das bibliotecas
import os # para uso de recursos do sistema operacional;
import sqlite3 # Para trabalho com banco de dados;

# criando funções de conexão

def get_db_connection():
    # verificando se existe a pasta database;
    # se não existir a base de dados então deverá ser criada;
    if not os.path.exists('database'):
        os.makedirs('database')
    # verifica se existe o caminho para o banco dbsqlite.db então crie dentro da pasta database;
    if not os.path.exists('database/dbsqlite.db'):
        conn = sqlite3.connect('database/dbsqlite.db')
        # Após criar o caminho e o banco agora Chame a Função create_tables
        create_tables(conn)
    else:
        # se já existir o diretorio e a base então faça somente a conexão;
        conn = sqlite3.connect('database/dbsqlite.db')
        create_tables(conn)
        # e carregue todas as linhas que existem de registro de nosso banco de dados;
        conn.row_factory = sqlite3.Row
        return conn
    

def create_tables(conn):
    # Criando a tabela CATEGORIAS
    conn.execute('''
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            img BLOB,
            ativo INTEGER
        )
    ''')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            img BLOB,
            id_cat INTEGER,
            ativo INTEGER,
            FOREIGN KEY (id_cat) REFERENCES categorias(id)
        )
    ''')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            senha TEXT NOT NULL,
            img BLOB,
            ativo INTEGER
        )
    ''')

    insert_initial_data(conn)
    
# se não existir dados na tabela então insira;
def insert_initial_data(conn):

    categorias = conn.execute('SELECT * FROM categorias').fetchall()


    # se não existir dados em CATEGORIAS então daremos um insert de dados ficticios no banco;
    if not categorias:
        conn.execute('''
        INSERT INTO categorias (nome, descricao)
            VALUES
                    ("Cat_PIZZA", "desc_PIZZA DOCE"),
                    ("Cat_SALGADOS", "desc_SALGADOS DA KITANDA")
        ''')

    conn.commit()
    
