from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'


from markupsafe import escape
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    print(url_for('profile', username='John Doe'))
        
#%%
from functools import wraps
def my_decorator(f):
    if f.__name__ == 'example':
        print(1)
        @wraps(f)
        def wrapper(*args, **kwds):
            print('Calling decorated function')
            return f(*args, **kwds)
        return wrapper
    else:
        print(2)
        @wraps(f)
        def wrapper(*args, **kwds):
            print('Calling decorated function', f.__name__)
            return f(*args, **kwds)
        return wrapper

@my_decorator
def example():
    """Docstring"""
    print('Called example function')

example()

@my_decorator
def example2():
    """Docstring"""
    print('Called example function2')
example2()
