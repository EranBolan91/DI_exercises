from flask import Flask
import pizza

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/home',default={'name':'stranger'})
@app.route('/home/<string:name>')
def home(name):
    return f'welcome home {name} '

@app.route('/pizza')
def make_pizza():
    return 'pizza has created'


def create_pizza():
    return 'pizza has created'

# @app.route('/custompizza/<path:args>')

if __name__ == "__main__":
    app.run()