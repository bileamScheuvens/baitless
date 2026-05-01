import os
import socket
import subprocess
import sys
from pathlib import Path

from flask import Flask

from baitless.constants import STORE

app = Flask(__name__)


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


@app.route("/favicon.ico")
def favicon():
    return "", 204


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def listen(path):
    success = open_video(path)
    if success:
        return f"playing {path}"
    return "Video not found :("


def open_video(video_name):
    full_path = os.path.join(STORE, video_name, video_name + ".mp4")
    if not Path(full_path).exists():
        return False
    if sys.platform.startswith("win"):
        os.startfile(full_path)
    elif sys.platform == "darwin":
        subprocess.run(["open", full_path])
    else:
        subprocess.run(["xdg-open", full_path])
    return True


def run_server():
    app.run(host="0.0.0.0", port=5000)
