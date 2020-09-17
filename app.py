from flask import Flask
from flask_hongshu import Crawler

app = Flask(__name__)

@app.route('/')
def index():
    c = Crawler()
    r = c.run()
    return r


if __name__ == "__main__":
    app.run(debug=True)