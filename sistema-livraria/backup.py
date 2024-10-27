import shutil, os
from constantes import BACKUPS_DIR, DB_PATH
from datetime import datetime

def fazer_backup():
    backup_file = BACKUPS_DIR / f'backup_livraria_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.db'
    
    shutil.copy(DB_PATH, backup_file)

    backups = sorted(BACKUPS_DIR.glob('*.db'), key=os.path.getctime, reverse=True)
    for backup in backups[5:]:
        backup.unlink()

def init_directories():
    BACKUPS_DIR.mkdir(parents=True, exist_ok=True)
