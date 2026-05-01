import json
from baitless.constants import DOWNLOAD_LIST

ANSI_GREEN = "\033[92m"
ANSI_RED = "\033[91m"
ANSI_END = "\033[0m"


def print_summary(downloaded, deleted):
    with open(DOWNLOAD_LIST) as f:
        download_list = json.loads(f.read())
    print("\n\n----- Summary: -----")
    for video in downloaded:
        print(f"{ANSI_GREEN}++ {video} {ANSI_END}")
    for video in download_list:
        if video in downloaded:
            continue
        print(video)
    for video in deleted:
        print(f"{ANSI_RED}-- {video} {ANSI_END}")
    print("\n----- Summary -----\n")
