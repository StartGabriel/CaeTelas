import sqlite3

def conectar(db_name):
    """Conecta ao banco de dados SQLite ou cria um novo banco de dados."""
    conn = sqlite3.connect(db_name)
    return conn

def criar_tabela(conn):
    """Cria a tabela user se não existir."""
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
    """Insere um novo usuário na tabela."""
    sql = """
    INSERT INTO user (nome, idade, email)
    VALUES (?, ?, ?);
    """
    conn.execute(sql, (nome, idade, email))
    conn.commit()

def consultar_user(conn, user_id):
    """Consulta um único usuário na tabela pelo user_id."""
    sql = "SELECT * FROM user WHERE user_id = ?;"
    cursor = conn.execute(sql, (user_id,))
    return cursor.fetchone()

def atualizar_user(conn, user_id, nome=None, idade=None, email=None):
    """Atualiza os dados de um usuário específico na tabela."""
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
    
    # Remover a última vírgula e espaço
    sql = sql.rstrip(', ')
    
    sql += " WHERE user_id = ?;"
    params.append(user_id)
    
    conn.execute(sql, params)
    conn.commit()

def deletar_user(conn, user_id):
    """Deleta um usuário específico na tabela."""
    sql = "DELETE FROM user WHERE user_id = ?;"
    conn.execute(sql, (user_id,))
    conn.commit()

