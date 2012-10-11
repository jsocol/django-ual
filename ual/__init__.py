try:
    from ual.utils import log_user_action
except ImportError:  # Happens during install.
    log_user_action = None


VERSION = (0, 1, 0)
__version__ = '.'.join(str(i) for i in VERSION)
__all__ = ['log_user_action']
