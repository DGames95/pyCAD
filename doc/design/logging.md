just use python logging module

### who logs stuff
SketchObject logs messages related to sketch solving, sketch object adition, etc.

Basically all 3D objects will log errors

## Interactive mode:
basically, I want a globa mode whereby if active, certain errors and warnings will not be silently
handled and logged, they will pop up, and ask for user input on how to handle it

## setup

setup function in main.py for now

should follow root logger level.

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


### Disable dependency debug logs e.g. Matplotlib

Set matplotlib's logger to warning level (this will show warnings and errors, but not info or debug messages)

    matplotlib_logger = logging.getLogger('matplotlib')
    matplotlib_logger.setLevel(logging.WARNING)