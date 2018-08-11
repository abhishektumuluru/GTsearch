# GTsearch commands shortcut logic

__version__ = "1.0.0"
__author__ = "Abhishek Tumuluru"
__email__ = "abhishek.tumuluru@gatech.edu"


class AttributeWrapper:
    """
    Add attributes to all command functions at once like their shortcut name
    or autocorrect
    """
    def decorate_all(decorator):
        # Decorate all callables in a class
        def wrapper(cls):
            for attr in cls.__dict__:
                func = getattr(cls, attr)
                if callable(func):
                    setattr(cls, attr, decorator(func))
            return cls
        return wrapper

    def assign_command_shortcut():
        def assign(func):
            if func.__name__ == "define":
                func.shortcut = "def"
            elif func.__name__ == "stock":
                func.shortcut = "$"
            elif func.__name__ == "buzzport":
                func.shortcut = "b"
            elif func.__name__ == "t-square":
                func.shortcut = "t"
            elif func.__name__ == "canvas":
                func.shortcut = "c"
            elif func.__name__ == "reddit":
                func.shortcut = "r"
            # Add other potential specific shortcuts here
            else:
                func.shortcut = func.__name__
            return func
        return assign

    def set_autocorrect():
        def assign(func):
            if len(func.shortcut) > 5:
                # Only attempt to autocorrect long shortcuts
                func.enable_autocorrect = True
            else:
                func.enable_autocorrect = False
            return func
        return assign


@AttributeWrapper.decorate_all(AttributeWrapper.set_autocorrect())
@AttributeWrapper.decorate_all(AttributeWrapper.assign_command_shortcut())
class Command:
    """
    Class with functions to add handling logic for each shortcut command
    and returning urls to redirect to. Handing logic on server instead of
    client makes commands extendable at the cost of latency.

    TODO implement everything and maybe add Slack, Trello, Github
    """
    def stock(args):
        pass

    def tsquare(args):
        return 'http://t-square.gatech.edu/portal'

    def default(arg):
        # Default to google search
        return 'http://www.google.com/search?q={0}'.format(arg)

    def spotify(args):
        return 'http://open.spotify.com/search/results/{0}'.format(args)

    def news(args):
        pass

    def cal(args):
        pass

    def remindme(args):
        pass

    def syn(args):
        pass

    def define(arg):
        return 'https://www.google.com/search?q=define%3A+{0}'.format(arg)

    def yt(args):
        if args:
            return 'http://www.youtube.com/results?search_query={0}&search_type=&aq=-1&oq='.format(args)
        return 'http://www.youtube.com'

    def m(args):
        pass

    def reddit(args):
        pass

    def man(args):
        pass

    def java(args):
        pass

    def py(args):
        pass

    def matlab(args):
        pass

    def canvas(args):
        pass

    def p(args):
        pass

    def mfp(args):
        pass

    def drive(args):
        pass

    def drop(args):
        pass

    def help(args):
        pass

    def fb(arg):
        if arg:
            return '''http://www.fb.com/search/top/?q={0}'''.format(arg)
        return 'http://www.fb.com'

    def menu(args):
        return 'https://www.gatechdining.com/dining-near-me/open-now'

    def room(args):
        return 'https://gtevents.gatech.edu/EmsWebApp/RoomRequest.aspx'

    def buzzport(args):
        return 'https://buzzport.gatech.edu/cp/home/displaylogin'

    def timer(args):
        pass

    def dw(args):
        pass

    def tw(args):
        pass

    def wiki(args):
        pass

    def ride(args):
        return 'https://gt-new.ridecell.com/request'

    def gmaps(args):
        pass

    def mail(args):
        pass

    def courseoff(args):
        pass


def test_attribute_wrapper(output=True):
    if output:
        for attr in Command.__dict__:
            if callable(getattr(Command, attr)):
                print(getattr(Command, attr).shortcut,
                      getattr(Command, attr).enable_autocorrect)


if __name__ == "__main__":
    test_attribute_wrapper()
