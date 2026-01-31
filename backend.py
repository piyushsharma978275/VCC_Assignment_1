from flask import Flask, jsonify

app = Flask(__name__)

# Hard-coded data
DATA = {
    "service": "Backend Microservice",
    "version": "1.0",
    "owner": "Piyush",
    "items": [
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Keyboard"},
        {"id": 3, "name": "Mouse"}
    ]
}

@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(DATA)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)