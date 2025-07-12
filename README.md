# Auto TikTok Shorts Generator 🎥🤖

This project is a fully automated TikTok shorts video generator. It uses AI to:
- generate engaging content,
- convert it to speech,
- find relevant video footage,
- and publish it with a shortened monetized link.

Perfect for those seeking passive income via content automation.

---

## 🧠 Features

- Topic selection powered by OpenAI GPT.
- Voice generation with ElevenLabs TTS.
- Visual content from Pexels API.
- Link monetization via Ouo.io.
- Full video generation with `moviepy`.

---

## 🚀 Setup

1. Clone the repository:
```bash
git clone https://github.com/dungangacore/tiktok-auto-generator.git
cd tiktok-auto-generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Add your API keys to a `config.py` file:
```python
# config.py (EXAMPLE)
PEXELS_API_KEY = "your_pexels_api_key"
OUO_API_KEY = "your_ouo_api_key"
ELEVENLABS_API_KEY = "your_elevenlabs_api_key"
OPENAI_API_KEY = "your_openai_api_key"
```

4. Run the bot:
```bash
python main.py
```

---

## 🖼️ Example Output

![Example Screenshot](https://placehold.co/600x400?text=Sample+TikTok+Video)

---

## 📁 File Structure

- `main.py` — Orchestrates the content creation workflow
- `content_generator.py` — Topic + script generator (GPT)
- `text_to_speech.py` — ElevenLabs TTS
- `video_creator.py` — Clips and composes video
- `link_shortener.py` — Monetized URL shortener
- `config.py` — API keys (excluded via .gitignore)

---

## 📄 License

This project is for **educational and non-commercial use only**. Use responsibly.
