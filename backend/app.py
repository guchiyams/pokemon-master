from flask import Flask, render_template
from dotenv import load_dotenv
import os

app = Flask(__name__, static_folder="./static", template_folder="./templates")

@app.route("/")
def index():
    return render_template("pokemon.html")

@app.route("/pokemon.css")
def css():
    with open('./static/pokemon.css', 'r') as file:
        css_content = file.read()
    return css_content

@app.route("/pokemon.js")
def js():
    with open('./static/pokemon.js', 'r') as file:
        js_content = file.read()
    return js_content


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

load_dotenv()

if __name__ == '__main__':
    port = int(os.getenv('FLASK_RUN_PORT', 5000))
    app.run(host='0.0.0.0', port=port)