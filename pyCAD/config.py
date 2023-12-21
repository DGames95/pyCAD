"""
CAD config class is used throughout the project to store and retrieve configuration settings.

Define all settings in the init method of the CADConfig class.


"""
import logging
from dataclasses import dataclass


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

@dataclass
class CADConfig(metaclass=SingletonMeta):
    # default settings
    UNITS = "mm"  # Default units for measurements (e.g., "mm", "inch")
    interactive = False  # Enable or disable pop-up warnings
    log_level = logging.INFO
    console_logging = True  # print logs to console
