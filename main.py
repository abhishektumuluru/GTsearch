# GTsearch endpoint for redirecting urls

__version__ = "1.0.0"
__author__ = "Abhishek Tumuluru"
__email__ = "abhishek.tumuluru@gatech.edu"

import interpreter
from flask import request, Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    # TODO change to GTsearch help page
    return redirect("http://www.google.com")


@app.route('/q/')
def route():
    """
    Routing for main search functionality
    Search url structure is server/q/?search=<search_query>
    Use request.args.get to get the value of the search variable
    and then process it to redirect
    """
    try:
        search_query = str(request.args.get('search', ''))
        url_route = interpreter.get_redirect_url(search_query)
        return redirect(url_route)
    except Exception as e:
        print(repr(e))
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
