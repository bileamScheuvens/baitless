import os
import json
from baitless.constants import DOWNLOAD_LIST, preview_dir, video_path

from yt_dlp import YoutubeDL


def download(name, url):
    os.makedirs(preview_dir(name), exist_ok=True)
    ydl = YoutubeDL(params={"format": "mp4", "outtmpl": video_path(name)})
    ydl.download(url)


def download_all():
    with open(DOWNLOAD_LIST) as f:
        download_list = json.loads(f.read())
    for video_name, url in download_list.items():
        print(video_name, url)
        print(os.path.exists(video_name))
        if os.path.exists(video_path(video_name)):
            print(f"{video_name} already downloaded.")
            continue
        download(video_name, url)


download_all()
