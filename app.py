from flask import Flask

app = Flask(__name__)


@app.route('/')
def classmusic():
    return 'cl4ss musik ön ßandcamp'
