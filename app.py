from flask import Flask, render_template
import requests

app = Flask(__name__)

BACKEND_URL = "http://192.168.1.101:5000/data"  # VM-1 IP

@app.route("/")
def index():
    response = requests.get(BACKEND_URL)
    data = response.json()
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
