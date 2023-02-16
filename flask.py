# APP.PY FILE CODE

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/myString")
def myfirstapi():
    return "String object returned and converted to HTML lang "


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    name = "Manav"
    return render_template("about.html", nameIs=name)


if __name__ == '__main__':
    app.run()
