from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hello from a Docker container - Version 2</h1><p>Built by AWS CodeBuild, stored in Amazon ECR - Arnav Gandhi</p>"


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)