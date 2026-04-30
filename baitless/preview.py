import cv2
from PIL import Image
from qrcode import QRCode
import random
import fpdf
from baitless.constants import preview_dir, video_path, preview_path, STORE
import os


def get_frames(video_name, n_frames=4):
    """Get random chronological frames from a video to act as preview."""
    cap = cv2.VideoCapture(video_path(video_name))
    total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    chunksize = total_frames // n_frames
    frames = []
    for i in range(n_frames):
        # get random frame from segment
        frame = random.randint(int(i * chunksize), int((i + 1) * chunksize))
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame)
        success, image = cap.read()
        if success:
            frames.append(image)
            cv2.imwrite(os.path.join(preview_dir(video_name), f"{i}.jpg"), image)
    return frames


# get_frames("tom.mp4")
def generate_preview(video_name, base_url):
    if os.path.exists(preview_path(video_name)):
        # return
        pass
    pdf = fpdf.FPDF()
    pdf.set_margin(0)
    margin = 15
    pdf.add_page()
    pdf.set_font("Helvetica", size=50, style="I")
    with pdf.local_context(text_mode="STROKE", line_width=2):
        pdf.set_y(margin)
        pdf.cell(
            text=f"{video_name.replace('_', ' ').title()}",
            center=True,
        )
    frames = get_frames(video_name, 4)
    n_rows = 2

    pdf.set_y(3 * margin)
    im_width = (pdf.epw - 2.25 * margin) / n_rows
    for i, frame in enumerate(frames):
        pdf.image(
            Image.fromarray(frame[..., ::-1]),
            w=im_width,
            keep_aspect_ratio=True,
            x=margin + im_width * (i // n_rows),
        )
        if i % n_rows:
            pdf.set_y(3 * margin)

    qr = QRCode()
    qr.add_data(f"{base_url}/{video_name}")
    # qr.print_ascii()
    qr.make_image()
    pdf.image(
        qr.make_image()._img,
        keep_aspect_ratio=True,
        w=im_width,
        y=pdf.eph - im_width - 2 * margin,
        x=pdf.epw / 2 - im_width / 2,
    )

    pdf.output(preview_path(video_name))


def generate_all_previews(base_url):
    for video_name in os.listdir(STORE):
        generate_preview(video_name, base_url)
