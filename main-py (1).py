#!/usr/bin/env python

import time
import random
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    model = {"title": "Hello GCP."}
    # Default version with no delay or errors
    return render_template('index.html', model=model)


# Version with delay to trigger latency alert
def main_with_delay():
    model = {"title": "Hello GCP."}
    time.sleep(10)  # 10-second delay
    return render_template('index.html', model=model)


# Version with random errors to trigger error alert
def main_with_errors():
    num = random.randrange(49)
    if num == 0:
        return json.dumps({"error": 'Error thrown randomly'}), 500
    else:
        model = {"title": "Hello GCP."}
        return render_template('index.html', model=model)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
