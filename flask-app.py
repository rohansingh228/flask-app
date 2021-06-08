from html import escape

from flask import Flask, redirect

app = Flask(__name__)

strings = ''


@app.route('/')
def hello_world():
    return 'Add a name in the URL to concatenate it with others'


@app.route('/<string:s>')
def concat_and_return(s):
    global strings
    if s != 'favicon.ico':
        strings += escape(s) + " "
    redirect('/')
    return strings


if __name__ == '__main__':
    app.run()
