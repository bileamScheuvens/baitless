import json
import os
import shutil

from baitless.constants import DOWNLOAD_LIST, STORE, preview_path, video_path


def delete_video(video_name):
    shutil.rmtree(os.path.dirname(video_path(video_name)))
    os.remove(preview_path(video_name))


def garbage_collect():
    with open(DOWNLOAD_LIST) as f:
        download_list = json.loads(f.read())

    deleted = []
    for video_name in os.listdir(STORE):
        if video_name in download_list or video_name == ".gitkeep":
            continue
        delete_video(video_name)
        deleted.append(video_name)
    return deleted
