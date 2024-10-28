from db_utils import adicionar_livro, exibir_livros, atualizar_preco, remover_livro, buscar_por_autor, algum_livro
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
            adicionar_livro(titulo, autor, ano, preco)
            fazer_backup()
        
        elif escolha == "2":
            if algum_livro():
                exibir_livros()
            else:
                print("\nNenhum livro cadastrado para exibir. Experimente adicionar um através da opção '1'.")

        elif escolha == "3":
            if algum_livro():
                id_livro = int(input("ID do livro a ser atualizado: "))
                novo_preco = float(input("Novo preço: "))
                atualizar_preco(id_livro, novo_preco)
                fazer_backup()
            else:
                print("\nNenhum livro cadastrado para atualizar. Experimente adicionar um através da opção '1'.")

        elif escolha == "4":
            if algum_livro():
                id_livro = int(input("ID do livro a ser removido: "))
                remover_livro(id_livro)
                fazer_backup()
            else:
                print("\nNenhum livro cadastrado para remover. Experimente cadastrar um através da opção '1'.")

        elif escolha == "5":
            if algum_livro():
                autor = input("Nome do autor: ")
                buscar_por_autor(autor)
            else:
                print("\nNenhum livro cadastro para buscar. Experimente cadastrar um através da opção '1'.")

        elif escolha == "6":
            if algum_livro():
                exportar_para_csv()
            else:
                print("\nNenhum livro cadastro para exportar. Experimente cadastrar um através da opção '1'.")

        elif escolha == "7":
            csv_path = input("Caminho do arquivo CSV a ser importado: ")
            importar_de_csv(csv_path)

        elif escolha == "8":
            if algum_livro():
                fazer_backup()
            else:
                print("\nNenhum livro cadastrado para armazenar numa cópia de segurança. Experimente cadastrar um através da opção '1'.")

        elif escolha == "9":
            break

        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    criar_estrutura()
    criar_db()
    menu()
