import os
from baitless.server import get_ip, run_server
from baitless.preview import generate_all_previews


if __name__ == "__main__":
    ip = get_ip()
    port = 5000
    generate_all_previews(base_url=f"http://{ip}:{port}")

    run_server()
