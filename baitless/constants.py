import os

ROOT = os.path.join(os.path.dirname(__file__), "..")
STORE = os.path.join(ROOT, "store")
DOWNLOAD_LIST = os.path.join(ROOT, "download_list.json")


def video_path(video_name):
    return os.path.join(STORE, video_name, f"{video_name}.mp4")


def preview_dir(video_name):
    return os.path.join(STORE, video_name, "frames")


def preview_path(video_name):
    return os.path.join(ROOT, "previews", f"{video_name}.pdf")
