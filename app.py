from flask import Flask, render_template
import os, socket

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html",
        hostname=socket.gethostname(),      # container ID when run in Docker
        version=os.getenv("APP_VERSION", "dev"),
    )


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
