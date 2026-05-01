import json
import os

from yt_dlp import YoutubeDL

from baitless.constants import DOWNLOAD_LIST, preview_dir, video_path


def download(name, url):
    os.makedirs(preview_dir(name), exist_ok=True)
    ydl = YoutubeDL(params={"format": "mp4", "outtmpl": video_path(name)})
    ydl.download(url)


def download_all():
    with open(DOWNLOAD_LIST) as f:
        download_list = json.loads(f.read())
    downloaded = []
    for video_name, url in download_list.items():
        if os.path.exists(video_path(video_name)):
            continue
        download(video_name, url)
        downloaded.append(video_name)
    return downloaded
