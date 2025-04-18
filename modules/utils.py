# modules/utils.py

import logging

def setup_logging(log_file='logs/app.log'):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='a'
    )
    logging.info("Logging initialized.")
