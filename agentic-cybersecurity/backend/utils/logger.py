import logging


logging.basicConfig(
    filename='outputs/logs/system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def log_message(message):

    logging.info(message)

    print(message)