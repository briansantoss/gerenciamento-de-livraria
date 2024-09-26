from pathlib import Path

def init_directories():
    data_dir = Path('./data')
    backups_dir = Path('./backups')
    exports_dir = Path('./exports')
    
    data_dir.mkdir(parents=True, exist_ok=True)
    backups_dir.mkdir(parents=True, exist_ok=True)
    exports_dir.mkdir(parents=True, exist_ok=True)
