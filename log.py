import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
    handlers=[
        logging.FileHandler("vizion.log"), # Saves logs to this file
        logging.StreamHandler()             # Prints logs to your console screen
    ]
)

# 2. This is the simple shortcut object you will import elsewhere
log = logging.getLogger()

