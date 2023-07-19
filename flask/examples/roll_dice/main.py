from random import randint
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def main():
    number = randint(1, 6)
    return render_template('index.html', result=number)

app.run()