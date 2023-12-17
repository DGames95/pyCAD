import logging
import os

from .config import CADConfig


def setup_logging(log_folder, log_level, console_logging):
    # Create the master logging folder if it doesn't exist
    if log_folder and not os.path.exists(log_folder):
        os.makedirs(log_folder)

    # Define the log file name and path
    log_file = os.path.join(log_folder, "pycad.log")

    # Configure the logging system
    logging.basicConfig(
        filename=log_file if log_folder else None,
        level=log_level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    if console_logging:
        # Configure the console logger for debugging purposes
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_formatter = logging.Formatter("%(levelname)s: %(message)s")
        console_handler.setFormatter(console_formatter)

        logger = logging.getLogger()
        logger.addHandler(console_handler)

if __name__ == "__main__":
    # Configure logging
    log_folder = CADConfig.log_directory  # Set master logging folder here
    log_level = CADConfig.log_level  # (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    console_logging = True  # True to enable console logging, False to disable

    if log_folder or console_logging:
        setup_logging(log_folder, log_level, console_logging)

    logging.debug("test_log")
    
