from pathlib import Path

# Armazena o caminho absoluto para a pasta do projeto (sistema-livraria)
PROJETO_PATH = Path(__file__).resolve().parent

DATA_DIR = PROJETO_PATH / "data"
BACKUPS_DIR = PROJETO_PATH / "backups"
EXPORTS_DIR = PROJETO_PATH / "exports"
DB_PATH = DATA_DIR / "livraria.db"

STRING_OPCOES = """
        1. Adicionar novo livro
        2. Exibir todos os livros
        3. Atualizar preço de um livro
        4. Remover um livro
        5. Buscar livros por autor
        6. Exportar dados para CSV
        7. Importar dados de CSV
        8. Fazer backup do banco de dados
        9. Sair
        """