from flask import Flask
from config import Config, DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)


@app.route('/')
def home():
    return '<h1>Home</h1>'


if __name__ == '__main__':
    app.run()
