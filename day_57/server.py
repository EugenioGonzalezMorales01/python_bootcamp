import datetime
import requests
from flask import Flask, render_template
import random
app = Flask(__name__)

def API_request(name):
    respose = requests.get(f"https://api.genderize.io?name={name}")
    return respose.json()

@app.route("/guess/<name>")
def home(name=None):
    random_number = random.randint(1, 10)
    actual_year = datetime.datetime.now().year
    user_info = API_request(name)
    return render_template("index.html", random_number=random_number, act_year=actual_year, name=str.capitalize(name), user_info=user_info)

@app.route("/blog/<num>")
def blog(num):
    print(num)
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_post = response.json()
    return render_template("blog.html", posts=all_post)

if __name__ == "__main__":
    app.run(debug=True)

API_request("peter")