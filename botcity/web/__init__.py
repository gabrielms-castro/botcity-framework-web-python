from .bot import *  # noqa: F401, F403

from botcity.web._version import get_versions
__version__ = get_versions()['version']
del get_versions
