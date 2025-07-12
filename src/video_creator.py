import os, requests, random, textwrap
from moviepy.editor import *
from PIL import Image
import moviepy.config as mpyconf
from config import PEXELS_API_KEY

class VideoCreator:
    def __init__(self):
        mpyconf.change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})
        if not hasattr(Image, "ANTIALIAS"):
            Image.ANTIALIAS = Image.Resampling.LANCZOS

    def fetch_image(self, query: str = "space") -> str:
        headers = {"Authorization": PEXELS_API_KEY}
        url = f"https://api.pexels.com/v1/search?query={query}&per_page=15"
        try:
            response = requests.get(url, headers=headers).json()
            img_url = random.choice(response["photos"])["src"]["portrait"]
            img_data = requests.get(img_url).content
            with open("pexels_bg.jpg", "wb") as f:
                f.write(img_data)
            return "pexels_bg.jpg"
        except:
            return None

    def create_video(self, content: str) -> None:
        if not os.path.exists("voice.mp3"):
            print("voice.mp3 not found.")
            return
        audio = AudioFileClip("voice.mp3")
        bg_image = self.fetch_image("space")
        if not bg_image:
            print("Background image failed.")
            return
        image_clip = ImageClip(bg_image).set_duration(audio.duration).resize(height=1920).set_position("center").set_audio(audio)
        text = content.split("Text:")[-1].strip()
        wrapped_text = textwrap.fill(text, width=50)
        txt_clip = TextClip(wrapped_text, fontsize=60, color="white", size=(1000, None), method="caption", font="Arial")
        txt_clip = txt_clip.set_position("center").set_duration(audio.duration)
        final_video = CompositeVideoClip([image_clip, txt_clip])
        final_video.write_videofile("output/output_video.mp4", fps=24)
