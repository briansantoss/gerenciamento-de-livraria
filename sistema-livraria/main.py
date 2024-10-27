from db import adicionar_livro, exibir_livros, atualizar_preco, remover_livro, buscar_por_autor
from backup import fazer_backup
from constantes import STRING_OPCOES
from csv_utils import exportar_para_csv, importar_de_csv
from init import criar_estrutura, criar_db

def menu():
    while True:
        print(STRING_OPCOES)
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            ano = int(input("Ano de publicação: "))
            preco = float(input("Preço: "))
            fazer_backup()
            adicionar_livro(titulo, autor, ano, preco)
        
        elif escolha == "2":
            exibir_livros()

        elif escolha == "3":
            id_livro = int(input("ID do livro a ser atualizado: "))
            novo_preco = float(input("Novo preço: "))
            fazer_backup()
            atualizar_preco(id_livro, novo_preco)

        elif escolha == "4":
            id_livro = int(input("ID do livro a ser removido: "))
            fazer_backup()
            remover_livro(id_livro)

        elif escolha == "5":
            autor = input("Nome do autor: ")
            buscar_por_autor(autor)
                

        elif escolha == "6":
            exportar_para_csv()

        elif escolha == "7":
            csv_path = input("Caminho do arquivo CSV a ser importado: ")
            importar_de_csv(csv_path)

        elif escolha == "8":
            fazer_backup()

        elif escolha == "9":
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    criar_estrutura()
    criar_db()
    menu()
