just use python logging module


setup function in main.py for now

to add log for a class:

    class LogTest():
        def __init__(self):
            self.logger = logging.getLogger(__name__)
            self.logger.debug("test")

### notes on speed

Use lazy formatting for log messages. Instead of:

    logger.debug("Processed data: " + str(data))

Use:

    logger.debug("Processed data: %s", data)

This way, the string concatenation and conversion only occur if the message is actually going to be logged.
