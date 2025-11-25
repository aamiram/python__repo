import os
import shutil
import time
from datetime import datetime

# directory wana backup
DIRECTORIES_TO_BACKUP = [
    r"C:\Users\YourName\Documents\project",
    r"C:\Users\YourName\Pictures"
]

#mysql dala
MYSQL_USER = "root"
MYSQL_PASSWORD = "yourpassword"
MYSQL_DATABASE = "yourdb"

# Output folder for all backups
BACKUP_FOLDER = "backups"

#main

# Create backup folder if not exists
if not os.path.exists(BACKUP_FOLDER):
    os.makedirs(BACKUP_FOLDER)

# Timestamp for filenames
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_name = f"backup_{timestamp}"
backup_temp_folder = os.path.join(BACKUP_FOLDER, backup_name)

os.makedirs(backup_temp_folder)

#  Copy directories
for folder in DIRECTORIES_TO_BACKUP:
    if os.path.exists(folder):
        print(f"Copying: {folder}")
        shutil.copytree(folder, os.path.join(backup_temp_folder, os.path.basename(folder)))
    else:
        print(f"Folder not found: {folder}")

#  Take MySQL database dump
dump_file = os.path.join(backup_temp_folder, f"{MYSQL_DATABASE}.sql")
dump_command = f'mysqldump -u{MYSQL_USER} -p{MYSQL_PASSWORD} {MYSQL_DATABASE} > "{dump_file}"'
print("Taking database backup...")
os.system(dump_command)

               # Compress backup folder
zip_filename = os.path.join(BACKUP_FOLDER, f"{backup_name}.zip")
print("Compressing backup...")
shutil.make_archive(zip_filename.replace(".zip", ""), 'zip', backup_temp_folder)

# Remove temporary folder
shutil.rmtree(backup_temp_folder)

print("\n Backup Completed Successfully!")
print(f"Saved As: {zip_filename}")
