from flask import Flask
          
def make_blod(func):
    def wrapper():
        return '<b>' + func() + '</b>'
    return wrapper

def make_emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

def make_underline(func):
    def wrapper():
        return '<u>' + func() + '</u>'
    return wrapper


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img width=200px src="https://www.rd.com/wp-content/uploads/2019/01/shutterstock_673465372.jpg?fit=700,467">'

# --- Use ---
# set FLASK_APP=hello.py
# $env:FLASK_APP = "hello.py"
# flask run

@app.route("/bye")
@make_blod
@make_emphasis
@make_underline
def bye():
    return "Bye"

@app.route("/greet/<name>")
def greet(name):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(debug=True)