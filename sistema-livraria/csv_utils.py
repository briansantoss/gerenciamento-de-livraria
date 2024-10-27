import csv
from db import sessao_db
from constantes import EXPORTS_DIR, DB_PATH

@sessao_db
def exportar_para_csv(cursor):
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()
    
    csv_path = EXPORTS_DIR / 'livros_exportados.csv'
    
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Título', 'Autor', 'Ano de Publicação', 'Preço'])
        writer.writerows(livros)
    
    print(f'Dados exportados para {csv_path}')

@sessao_db
def importar_de_csv(cursor, csv_path):
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            cursor.execute('''
                INSERT INTO livros (id, titulo, autor, ano_publicacao, preco)
                VALUES (?, ?, ?, ?, ?)
            ''', (row[0], row[1], row[2], row[3], row[4]))
    
    print(f'Dados importados de {csv_path}')
