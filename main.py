import random
from flask import Flask
from flask import render_template

app = Flask("Hello World")

if __name__ == "_main_":
    app.run(debug=True, port=5000)


@app.route("/")  ##wenn diese URL aufgerufen wird, soll etwas passieren
def hello():
    foo = ["Domingo", "Furkan", "Gianni", "Lukas", "Syd", "Nemro", "Manu"]
    name_choice_ = random.choice(foo)
    return render_template("index.html", name=name_choice_)
    # das wird dem Browser gesendet, wenn die URL aufgerufen wird


@app.route("/abouttest")
def about():
    return "<h1>about test</h1>"
