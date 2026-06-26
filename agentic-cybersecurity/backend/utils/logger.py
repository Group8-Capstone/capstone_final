import os
import logging

# =====================================
# CREATE LOG DIRECTORY IF NOT EXISTS
# =====================================

LOG_DIR = "outputs/logs"

os.makedirs(
    LOG_DIR,
    exist_ok=True
)

LOG_FILE = os.path.join(
    LOG_DIR,
    "system.log"
)

# =====================================
# CONFIGURE LOGGER
# =====================================

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def log_message(message):
    """
    Log a message to both the log file and console.
    """

    logging.info(message)

    print(message)
