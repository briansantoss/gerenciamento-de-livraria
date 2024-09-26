import csv
import sqlite3
from pathlib import Path

db_path = Path('./data/livraria.db')
exports_dir = Path('./exports')

def exportar_para_csv():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()
    
    csv_path = exports_dir / 'livros_exportados.csv'
    
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Título', 'Autor', 'Ano de Publicação', 'Preço'])
        writer.writerows(livros)
    
    conn.close()
    print(f'Dados exportados para {csv_path}')

def importar_de_csv(csv_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            cursor.execute('''
                INSERT INTO livros (id, titulo, autor, ano_publicacao, preco)
                VALUES (?, ?, ?, ?, ?)
            ''', (row[0], row[1], row[2], row[3], row[4]))
    
    conn.commit()
    conn.close()
    print(f'Dados importados de {csv_path}')
