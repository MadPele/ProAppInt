from flask import Flask, render_template, make_response

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/home')
def home_page():
    return render_template('home_page.html')


if __name__ == '__main__':
    app.run()
