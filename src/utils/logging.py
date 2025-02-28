import logging
import sys
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Create handlers
# 1) Console Handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)

# 2) Timed Rotating File Handler
file_handler = TimedRotatingFileHandler(
    LOG_DIR / "app.log",
    when="midnight",        # Rotate daily at midnight
    backupCount=7,          # Keep 7 days of logs
    encoding="utf-8"
)
file_handler.setLevel(logging.INFO)

# Create a main logger
logger = logging.getLogger("myproject")
logger.setLevel(logging.INFO)
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Example: If we want to also send logs to an external aggregator
# (Pseudo code: you'll adapt to Logfire’s actual API)
"""
def send_to_logfire(record):
    # Convert log record to JSON and send to Logfire endpoint
    pass

class LogfireHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        send_to_logfire(log_entry)

logfire_handler = LogfireHandler()
logfire_handler.setLevel(logging.WARNING)  # or INFO, etc.
logger.addHandler(logfire_handler)
"""

def get_logger(name):

    logger = logging.getLogger(name)

    # Set the logging level

    logger.setLevel(logging.INFO)

    # Create formatters

    formatter = logging.Formatter(

        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    )

    # Create and configure file handler

    file_handler = RotatingFileHandler(

        LOG_DIR / 'app.log',  # Log file path

        maxBytes=1024 * 1024,  # 1MB

        backupCount=5

    )

    file_handler.setFormatter(formatter)

    # Create and configure console handler

    console_handler = logging.StreamHandler(sys.stdout)

    console_handler.setFormatter(formatter)

    # Add handlers to logger if they haven't been added already

    if not logger.handlers:

        logger.addHandler(file_handler)

        logger.addHandler(console_handler)

    return logger

 
