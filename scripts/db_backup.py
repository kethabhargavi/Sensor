import shutil
from datetime import datetime

source = "sensordb.db"

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup = f"backup_sensordb_{timestamp}.db"

shutil.copy2(source, backup)

print(f"Database backup created: {backup}")
