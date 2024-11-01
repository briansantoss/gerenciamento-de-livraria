import sqlite3
from constantes import DB_PATH 

# Função com o propósito de estabelecer uma conexão com o banco de dados e a repassar para a função de argumento (funcao_arg)
def sessao_db(funcao_arg):
    def wrapper(*args, **kwargs):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            return funcao_arg(cursor, *args, **kwargs)
    return wrapper

@sessao_db
def algum_livro(cursor):
    cursor.execute("SELECT COUNT(*) FROM livros")

    # Verifica se existe algum livro registrado no banco
    num_livros = cursor.fetchone()[0]

    return True if num_livros > 0 else False

@sessao_db
def adicionar_livro(cursor, titulo, autor, ano_publicacao, preco):
    cursor.execute("""
        INSERT INTO livros (titulo, autor, ano_publicacao, preco)
        VALUES (?, ?, ?, ?)
    """, (titulo, autor, ano_publicacao, preco))

@sessao_db
def exibir_livros(cursor):
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    
    print("-"*40)
    
    for livro in livros:
        print(f"ID: {livro[0]}")
        print(f"Título: {livro[1]}")
        print(f"Autor: {livro[2]}")
        print(f"Ano de Publicação: {livro[3]}")
        print(f"Preço: {livro[4]}")
        print("-"*40)

@sessao_db
def atualizar_preco(cursor, id_livro, novo_preco):
    cursor.execute("""
        UPDATE livros SET preco = ? WHERE id = ?
    """, (novo_preco, id_livro))

    # Verificação da quantidade de registros afetados com o comando realizado, caso nula, exibe uma mensagem de erro
    num_livros = cursor.rowcount
    if num_livros == 0:
        print("ERRO: Nenhum livro com o id '{id_livro}' encontrado.")
        # Retorno mais cedo sem valor (elimina a necessidade de else)
        return

    print("Inserção realizada com sucesso.")
    
@sessao_db
def remover_livro(cursor, id_livro):
    cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro,))

    num_livros = cursor.rowcount
    if num_livros == 0:
        print("ERRO: Nenhum livro com o id '{id_livro}' encontrado.")
        return
    
    print("Remoção realizada com sucesso!")

@sessao_db
def buscar_por_autor(cursor, autor):
    cursor.execute("SELECT * FROM livros WHERE autor LIKE ?", ("%" + autor + "%",))
    
    livros = cursor.fetchall()
    
    print("-"*40)
    for livro in livros:
        print(f"ID: {livro[0]}")
        print(f"Nome: {livro[1]}")
        print(f"Autor: {livro[2]}")
        print(f"Ano de Publicação: {livro[3]}")
        print(f"Preço: {livro[4]}")
        print("-"*40)
