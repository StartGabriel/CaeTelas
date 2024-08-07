import sqlite3

def conectar(db_name):
    conn = sqlite3.connect(db_name)
    return conn

def criar_tabela(conn):
    sql = """
    CREATE TABLE IF NOT EXISTS user (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        email TEXT NOT NULL
    );
    """
    conn.execute(sql)
    conn.commit()

def inserir_user(conn, nome, idade, email):
    sql = """
    INSERT INTO user (nome, idade, email)
    VALUES (?, ?, ?);
    """
    conn.execute(sql, (nome, idade, email))
    conn.commit()

def consultar_users(conn):
    sql = "SELECT * FROM user;"
    cursor = conn.execute(sql)
    return cursor.fetchall()

def atualizar_user(conn, user_id, nome=None, idade=None, email=None):
    sql = "UPDATE user SET "
    params = []
    
    if nome:
        sql += "nome = ?, "
        params.append(nome)
    if idade:
        sql += "idade = ?, "
        params.append(idade)
    if email:
        sql += "email = ?, "
        params.append(email)
    

    sql = sql.rstrip(', ')
    
    sql += " WHERE user_id = ?;"
    params.append(user_id)
    
    conn.execute(sql, params)
    conn.commit()

def deletar_user(conn, user_id):
    sql = "DELETE FROM user WHERE user_id = ?;"
    conn.execute(sql, (user_id,))
    conn.commit()


