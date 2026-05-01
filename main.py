from baitless.download import download_all
from baitless.garbage_collect import garbage_collect
from baitless.preview import generate_all_previews
from baitless.server import get_ip, run_server
from baitless.summary import print_summary

if __name__ == "__main__":
    ip = get_ip()
    port = 5000
    deleted = garbage_collect()
    downloaded = download_all()
    generate_all_previews(base_url=f"http://{ip}:{port}")
    print_summary(downloaded, deleted)
    run_server()
