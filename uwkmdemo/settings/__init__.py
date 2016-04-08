import sys
import logging

from uwkmdemo.settings.base import *

try:
    from uwkmdemo.settings.local import *
except ImportError:
    pass
