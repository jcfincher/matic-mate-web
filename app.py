from flask import Flask, render_template, request, redirect
import json
import subprocess

app = Flask(__name__)

CONFIG_FILE = "config.json"

def load_config():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(data):
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/", methods=["GET", "POST"])
def index():
    config = load_config()

    if request.method == "POST":
        for key in config:
            config[key] = request.form.get(key)
        save_config(config)
        return redirect("/")

    return render_template("index.html", config=config)

@app.route("/call", methods=["POST"])
def call():
    subprocess.run(["python3", "make_call.py"])
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)