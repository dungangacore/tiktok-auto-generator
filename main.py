from src.content_generator import ContentGenerator
from src.text_to_speech import TextToSpeech
from src.video_creator import VideoCreator
from src.link_shortener import LinkShortener

def main():
    print("[1/5] Generating content...")
    generator = ContentGenerator()
    content = generator.generate()

    print("[2/5] Generating voice...")
    tts = TextToSpeech()
    tts.generate_voice(content)

    print("[3/5] Creating video...")
    creator = VideoCreator()
    creator.create_video(content)

    print("[4/5] Shortening link...")
    shortener = LinkShortener()
    short_url = shortener.shorten("https://instagram.com/")
    print("Shortened URL:", short_url)

    print("[5/5] Done. Video saved as output/output_video.mp4")

if __name__ == "__main__":
    main()
