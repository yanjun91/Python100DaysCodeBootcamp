from flask import Flask, render_template
import random
from datetime import datetime as dt
import requests


app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = dt.today().year
    return render_template("index.html", num=random_number, current_year=current_year)


@app.route("/guess/<name>")
def guess(name):
    agify_url = f"https://api.agify.io?name={name}"
    genderize_url = f"https://api.genderize.io?name={name}"
    agify_res = requests.get(url=agify_url)
    age_data = agify_res.json()
    age = age_data["age"]

    genderize_res = requests.get(url=genderize_url)
    gender_data = genderize_res.json()
    gender = gender_data["gender"]
    return render_template("guess.html", name=name, age=age, gender=gender)


@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/ed99320662742443cc5b"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
