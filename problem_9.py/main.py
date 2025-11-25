import schedule
import time
import logging
from datetime import datetime

#login
logging.basicConfig(
    filename="task_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# your task
def backup_task():
    logging.info("Running backup task...")
    print("Backup started at:", datetime.now())
    # your function code here
    # Example:
    # take_backup()
    # generate_passwords()
    # create_ssh_keys()
    print("Backup finished.")
# Scheduling Configurations


# Run every minute
schedule.every(1).minutes.do(backup_task)

# Run every hour
# schedule.every().hour.do(backup_task)

# Run every day at specific time
# schedule.every().day.at("23:00").do(backup_task)



# Main Loop
while True:
    schedule.run_pending()
    time.sleep(1)   # prevent CPU usage spike
