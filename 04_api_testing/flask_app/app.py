from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask API running 🚀"

@app.route("/health")
def health():
    return jsonify(status="OK", service="flask-api")

@app.route("/hello/<name>")
def hello(name):
    return jsonify(message=f"Hello {name} from Flask!")

if __name__ == "__main__":
    app.run(debug=True)
