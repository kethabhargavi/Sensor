import os

for filename in os.listdir("."):
    if filename.startswith("backup_sensordb_") and filename.endswith(".db"):
        print(f"Found backup: {filename}")
