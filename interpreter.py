# GTsearch search tokenize helper

__version__ = "1.0.0"
__author__ = "Abhishek Tumuluru"
__email__ = "abhishek.tumuluru@gatech.edu"
__status__ = "testing"


from Command import Command
from functools import lru_cache, wraps
import threading


def synchronize(lock):
    """Wrap function with lock acquire and release"""
    def wrapper(func):
        @wraps(func)
        def locked(*args, **kwargs):
            lock.acquire()
            try:
                return func(*args, **kwargs)
            finally:
                lock.release()
        return locked
    return wrapper


def create_shortcut_to_function_map():
    """
    Creating this map in case the name of the function is not
    the shortcut, like "$" for stock
    which cannot be a function declaration in Python
    """
    shortcut_to_function_map = dict()
    for cmd in Command.__dict__:
        cmd_function = getattr(Command, cmd)
        if callable(cmd_function):
            shortcut_to_function_map[cmd_function.shortcut] = cmd_function
            shortcut_to_function_map[cmd_function.__name__] = cmd_function
    return shortcut_to_function_map


def tokenize(search_query):
    """
    Split up a search query into a shortcut and its arguments
    from the first whitespace
    >>> tokenize("yt cat videos")
    >>> ['yt', 'cat videos']
    >>> tokenize("yt")
    >>> ['yt', None]
    >>> tokenize("")
    >>> None, None
    """
    if len(search_query) == 0:
        return None, None
    split_search_query = search_query.split(maxsplit=1)
    if len(split_search_query) == 1:
        return split_search_query[-1], None
    return split_search_query


shortcut_to_function_map = create_shortcut_to_function_map()


@synchronize(threading.Lock())
@lru_cache(maxsize=128, typed=False)
def get_redirect_url(search_query):
    # Use LRU cache to stash recent queries to save time for upcoming calls
    cmd, arg = tokenize(search_query)
    if cmd is None:
        return ''
    default = Command.default(cmd + ' ' + (arg or ''))
    if cmd in shortcut_to_function_map:
        try:
            # Get the relevant Command function pointer and invoke it on arg
            command_function = getattr(Command,
                                       shortcut_to_function_map[cmd].__name__)
            url = command_function.__call__(arg)
            if url is None:
                # If shortcut is not implemented but is present
                return Command.default(cmd + ' ' + (arg or ''))
            return url
        except TypeError as te:
            print(repr(te))
            return default
        except AttributeError as ae:
            print(repr(ae))
            return default
        except Exception as e:
            print(repr(e))
            return default
    return default


def autocorrect_shortcut(split_search_query):
    # TODO autocorrect a shortcut to the closest edit
    # distance shortcut in shortcut_to_function_map
    pass


def test_get_redirect_url_output(output=True):
    if output:
        print(get_redirect_url(""))
        print(get_redirect_url("nonexistentshortcut"))
        print(get_redirect_url("nonexistentshortcut hello"))
        print(get_redirect_url("yt cat videos"))
        print(get_redirect_url("room"))


if __name__ == '__main__':
    test_get_redirect_url_output()
