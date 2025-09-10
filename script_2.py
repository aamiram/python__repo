import shutil
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    #logging → is the module name (comes with Python).
    #basicConfig → is a function inside that module that sets up logging.

    filename="disk_usage.log",#.log is an extension
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
    # format here is a parameter(argument )
)

# Threshold in percentage
THRESHOLD = 80 

def check_disk_usage():
    total, used, free = shutil.disk_usage("c:\\")
    # The values returned by shutil.disk_usage("/") are fixed in a specific order:
    # the order is first = total  sec = used  third = free
    used_par = (used / total) * 100

    if used_par > THRESHOLD:
        logging.warning(f"Disk usage exceeded {THRESHOLD}%! Current: {used_par:.2f}%")
    else:
        logging.info(f"Disk usage is OK: {used_par:.2f}%")

if __name__ == "__main__":
    # __name__ is a built in function in python for every file
    check_disk_usage()
