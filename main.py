from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from the ADO Flask app!"

@app.route("/hello")
def hello():
    return "Hegadnjlbnad;kv adlknvda lgap!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)