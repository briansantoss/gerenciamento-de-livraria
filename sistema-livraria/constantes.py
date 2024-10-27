from pathlib import Path

DATA_DIR = Path('./data')
BACKUPS_DIR = Path('./backups')
EXPORTS_DIR = Path('./exports')
DB_PATH = Path('./data/livraria.db')

STRING_OPCOES = '''
        1. Adicionar novo livro
        2. Exibir todos os livros
        3. Atualizar preço de um livro
        4. Remover um livro
        5. Buscar livros por autor
        6. Exportar dados para CSV
        7. Importar dados de CSV
        8. Fazer backup do banco de dados
        9. Sair
        '''