import random

from flask import Flask
app = Flask(__name__)

winner = random.randint(0,9)

@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:number>')
def guess(number):
    if number < winner:
        return '<h1>Too low :(</h1>'
    if number > winner:
        return '<h1>Too high :/</h1>'
    if number == winner:
        return '<h1>YOU WIN</h1>'



if __name__ == "__main__":
    app.run(debug=True)