

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
    # Criando a tabela NOTÍCIAS
    conn.execute('''
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            img BLOB,
            resume TEXT,
            newsletter TEXT,
            ativo INTEGER
        )
    ''')



    insert_initial_data(conn)
    
# se não existir dados na tabela então insira;
def insert_initial_data(conn):

    news = conn.execute('SELECT * FROM news').fetchall()


    # se não existir dados em NEWS então daremos um insert de dados ficticios no banco;
    if not news:
        conn.execute('''
        INSERT INTO news (title, resume)
            VALUES
                    ("Concursos para Perito Criminal: 193 vagas autorizadas", "Como havíamos previsto, o ano passado foi recheado de oportunidades para Perito Criminal. A boa notícia é que 2024 não está sendo diferente."),
                    ("Forense Digital: profissão atua na investigação de crimes cibernéticos", "Sendo uma área em constante inovação e considerada uma das profissões do futuro, o trabalho de perícia forense digital permite a coleta de evidências.")
        ''')

    conn.commit()
    
