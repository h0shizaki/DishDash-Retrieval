from flask import Flask
app = Flask(__name__)

@app.route('/api')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'

@app.route('/api/b')
def hi_geek():
    return '<h1>Hello from Flask & Docker 2</h2>'

if __name__ == "__main__":
    app.run(debug=False)