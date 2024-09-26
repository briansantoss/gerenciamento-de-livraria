# Sistema de Gerenciamento de Livraria 📚

Este é um sistema completo de gerenciamento de uma livraria, que utiliza **SQLite** como banco de dados, manipulação de arquivos **CSV** e realiza **backups automáticos**. O projeto combina diversos conceitos, incluindo **CRUD**, manipulação de arquivos, exportação e importação de dados.

## Funcionalidades

1. **Adicionar novo livro**: Insere um novo registro de livro no banco de dados.
2. **Exibir todos os livros**: Lista todos os livros cadastrados.
3. **Atualizar preço de um livro**: Atualiza o preço de um livro específico.
4. **Remover um livro**: Remove um livro do banco de dados.
5. **Buscar livros por autor**: Busca todos os livros escritos por um autor específico.
6. **Exportar dados para CSV**: Exporta todos os livros cadastrados para um arquivo CSV.
7. **Importar dados de CSV**: Importa livros de um arquivo CSV para o banco de dados.
8. **Fazer backup do banco de dados**: Cria uma cópia de segurança do banco de dados.
9. **Limpeza de backups antigos**: Mantém apenas os 5 backups mais recentes e exclui os mais antigos.

## Estrutura do Projeto

A estrutura de diretórios segue a seguinte organização:

/meu_sistema_livraria/ /backups/ # Contém backups automáticos do banco de dados. backup_livraria_YYYY-MM-DD.db /data/ # Contém o banco de dados principal. livraria.db /exports/ # Contém arquivos CSV exportados. livros_exportados.csv


## Requisitos

- Python 3.x
- Bibliotecas: `sqlite3`, `pandas`, `csv`, `os`, `pathlib`
  
Para instalar as dependências, você pode usar o seguinte comando (caso necessário):

```bash
pip install pandas
