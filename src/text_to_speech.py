from gtts import gTTS

class TextToSpeech:
    def generate_voice(self, text: str) -> None:
        tts = gTTS(text.split("Text:")[-1].strip(), lang="en")
        tts.save("voice.mp3")
