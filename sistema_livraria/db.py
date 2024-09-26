import sqlite3
from pathlib import Path

db_path = Path('./data/livraria.db')

def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano_publicacao INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_livro(titulo, autor, ano_publicacao, preco):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO livros (titulo, autor, ano_publicacao, preco)
        VALUES (?, ?, ?, ?)
    ''', (titulo, autor, ano_publicacao, preco))
    conn.commit()
    conn.close()

def exibir_livros():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()
    
    print('-'*40)
    
    for livro in livros:
        print(f'ID: {livro[0]}')
        print(f'Título: {livro[1]}')
        print(f'Autor: {livro[2]}')
        print(f'Ano de Publicação: {livro[3]}')
        print(f'Preço: {livro[4]}')
        print('-'*40)
        
    conn.close()

def atualizar_preco(id_livro, novo_preco):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE livros SET preco = ? WHERE id = ?
    ''', (novo_preco, id_livro))
    conn.commit()
    conn.close()

def remover_livro(id_livro):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM livros WHERE id = ?', (id_livro,))
    conn.commit()
    conn.close()

def buscar_por_autor(autor):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros WHERE autor LIKE ?', ('%' + autor + '%',))
    livros = cursor.fetchall()
    
    print('-'*40)
    for livro in livros:
        print(f'ID: {livro[0]}')
        print(f'Nome: {livro[1]}')
        print(f'Autor: {livro[2]}')
        print(f'Ano de Publicação: {livro[3]}')
        print(f'Preço: {livro[4]}')
        print('-'*40)
    
    conn.close()
