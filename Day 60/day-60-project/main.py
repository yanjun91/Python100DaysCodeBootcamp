import smtplib

from flask import Flask, render_template, request
import requests
import os

posts = requests.get("https://api.npoint.io/83204665af6bb9e1d0e4").json()
SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")
RECIPIENT_EMAIL = "yanjun_5473@hotmail.com"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:post_id>")
def blogpost(post_id):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == post_id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/form-entry", methods=['POST'])
def receive_data():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    send_email(name, email, phone, message)
    return render_template("contact.html", msg_sent=True)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(SENDER_EMAIL, SENDER_PASSWORD)
        connection.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True)
