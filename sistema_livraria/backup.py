import shutil
from pathlib import Path
from datetime import datetime
import os

backups_dir = Path('./backups/')
db_path = Path('./data/livraria.db')

def fazer_backup():
    backup_file = backups_dir / f'backup_livraria_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.db'
    
    shutil.copy(db_path, backup_file)

    backups = sorted(backups_dir.glob('*.db'), key=os.path.getctime, reverse=True)
    for backup in backups[5:]:
        backup.unlink()

def init_directories():
    backups_dir.mkdir(parents=True, exist_ok=True)
