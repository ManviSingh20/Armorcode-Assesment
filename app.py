from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    with open("README.md", "r") as f:
        return f.read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
  
