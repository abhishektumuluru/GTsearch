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
        # Decorate all callables in a class, used for functions here
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
            elif func.__name__ == "stack_overflow":
                func.shortcut = "st"
            elif func.__name__ == "stack_overflow_lucky":
                func.shortcut = "stl"
            elif func.__name__ == "wikipedia":
                func.shortcut = "w"
            elif func.__name__ == "twitter":
                func.shortcut = "tw"
            elif func.__name__ == "courseoff":
                func.shortcut = "co"
            elif func.__name__ == "spotify":
                func.shortcut = "spot"
            elif func.__name__ == "matlab":
                func.shortcut = "mat"
            # add other potential specific shortcuts here
            else:
                func.shortcut = func.__name__
            return func
        return assign

    def set_autocorrect():
        def assign(func):
            if len(func.shortcut) > 5 or len(func.__name__) > 5:
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
    Context menu in extension for TinyURL, Wikipedia
    """
    def help(args):
        pass

    def news(args):
        pass

    def syn(args):
        pass

    def java(args):
        pass

    def py(args):
        pass

    def p(args):
        pass

    def mfp(args):
        pass

    def canvas(args):
        return 'https://gatech.instructure.com/'

    def msg(args):
        if args:
            return 'https://www.messenger.com/?qa={0}'.format(args)
        return 'https://www.messenger.com/'

    def matlab(args):
        if args:
            return 'https://www.mathworks.com/help/search.html?qdoc={0}&submitsearch='.format(args)
        return 'https://www.mathworks.com/help/'

    def drive(args):
        return 'https://drive.google.com/drive/my-drive'

    def man(arg):
        if arg:
            return 'http://ss64.com/bash/{0}.html'.format(arg)
        return 'http://ss64.com/bash/'

    def stock(arg):
        if arg:
            return 'http://finance.yahoo.com/quote/{0}'.format(arg)
        return 'http://finance.yahoo.com/'

    def im_feeling_lucky(args):
        if args:
            return 'http://www.google.com/search?btnI=1&q={0}'.format(args)
        return 'http://www.google.com/search?btnI=1&q='

    def tsquare(args):
        return 'http://t-square.gatech.edu/portal'

    def default(arg):
        # Default to google search
        return 'http://www.google.com/search?q={0}'.format(arg)

    def spotify(args):
        if args:
            return 'http://open.spotify.com/search/results/{0}'.format(args)
        return 'http://open.spotify.com/collection/playlists'

    def define(arg):
        return 'https://www.google.com/search?q=define%3A+{0}'.format(arg)

    def cal(args):
        return 'https://calendar.google.com/calendar/r'

    def yt(args):
        if args:
            return 'http://www.youtube.com/results?search_query={0}&search_type=&aq=-1&oq='.format(args)
        return 'http://www.youtube.com'

    def reddit(args):
        if args:
            args_split = args.split(maxsplit=1)
            if len(args_split) == 1:
                return 'http://www.reddit.com/r/{0}'.format(args)
            return 'http://www.reddit.com/r/{0}/search?q={1}&restrict_sr=1'.format(args_split[0], args_split[1])
        return 'http://www.reddit.com/'

    def fb(arg):
        if arg:
            return 'http://www.fb.com/search/top/?q={0}'.format(arg)
        return 'http://www.fb.com'

    def menu(args):
        return 'https://www.gatechdining.com/dining-near-me/open-now'

    def room(args):
        return 'https://gtevents.gatech.edu/EmsWebApp/RoomRequest.aspx'

    def buzzport(args):
        return 'https://buzzport.gatech.edu/cp/home/displaylogin'

    def timer(args):
        if args:
            return 'https://www.online-stopwatch.com/timer/{0}'.format(args)
        return Command.default("timer")

    def stack_overflow(args):
        if args:
            return Command.default('{0} site:stackoverflow.com'.format(args))
        return 'http://www.stackoverflow.com/'

    def stack_overflow_lucky(args):
        # Will attempt I'm feeling lucky if there is high confidence
        if args:
            return '{0} site:stackoverflow.com'.format(Command.im_feeling_lucky(args))
        return 'http://www.stackoverflow.com/'

    def dw(args):
        return 'https://login.gatech.edu/cas/login?service=https%3A%2F%2Fdegreeaudit.gatech.edu'

    def twitter(arg):
        if arg:
            return 'https://twitter.com/{0}'.format(arg)
        return 'https://twitter.com/'

    def wikipedia(args):
        try:
            if args:
                import wikipedia
                results = wikipedia.search(args, results=1, suggestion=True)
                if len(results[0]) > 0:
                    page = wikipedia.page(results[0][0])
                else:
                    page = wikipedia.page(args)
                return page.url
            return 'http://www.wikipedia.org/'
        except ImportError:
            return 'https://www.wikipedia.org/'

    def ride(args):
        return 'https://gt-new.ridecell.com/request'

    def gmaps(args):
        if args:
            return 'http://www.google.com/maps/search/{0}'.format(args)
        return 'http://www.google.com/maps/search/'

    def mail(args):
        return 'http://www.mail.gatech.edu'

    def courseoff(args):
        return 'http://gatech.courseoff.com/workspace'

    def stamps(args):
        return 'http://login.gatech.edu/cas/login?TARGET=https%3a%2f%2fwww.myappointment.health.gatech.edu%2fdefault.aspx'

    def jobs():
        return 'https://gatech-csm.symplicity.com/students/index.php?s=home'


def test_attribute_wrapper(output=True):
    if output:
        for attr in Command.__dict__:
            if callable(getattr(Command, attr)):
                print(getattr(Command, attr).shortcut,
                      getattr(Command, attr).enable_autocorrect)


if __name__ == "__main__":
    test_attribute_wrapper()
