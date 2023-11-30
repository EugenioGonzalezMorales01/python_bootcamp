from flask import Flask, render_template
import post

app = Flask(__name__)
all_posts = post.Post().posts
@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:e_post>')
def specific_post(e_post):
    for post in all_posts:
        if post["id"] == e_post:
            e_post = post
    return render_template('post.html', post=e_post)

if __name__ == "__main__":
    app.run(debug=True)
