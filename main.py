# Importing flask module in the project is mandatory
from flask import Flask

# An object of Flask class is our WSGI application.
# Flask constructor takes the name of the current module (name) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call the associated function.
@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/')
# / URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

# Main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='0.0.0.0', port=5000, debug=True)