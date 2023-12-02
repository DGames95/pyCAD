just use python logging module


setup function in main.py for now

to add log for a class:

class LogTest():
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug("test")

