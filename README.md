# 🎥🤖 Auto TikTok Shorts Generator

A fully automated TikTok shorts generator powered by AI. It:

- 🎯 Generates engaging content using GPT
- 🎤 Converts text to speech using ElevenLabs
- 🎞️ Fetches relevant video clips from Pexels
- 💰 Adds monetized links with Ouo.io
- 📹 Produces ready-to-upload short videos

Perfect for passive income through automated content creation.

---

## 🧠 Features

- AI-generated topics and scripts via **OpenAI GPT**
- Realistic voice narration using **ElevenLabs TTS**
- Stock footage from **Pexels API**
- Monetized URL shortening with **Ouo.io**
- Final video creation handled by **moviepy**

---

## 🚀 Setup

1. **Clone the repository**  
```bash
git clone https://github.com/dungangacore/tiktok-auto-generator.git
cd tiktok-auto-generator
```

2. **Install dependencies**  
```bash
pip install -r requirements.txt
```

3. **Create your `config.py` with API keys**  
```python
# config.py (EXAMPLE)
PEXELS_API_KEY = "your_pexels_api_key"
OUO_API_KEY = "your_ouo_api_key"
ELEVENLABS_API_KEY = "your_elevenlabs_api_key"
OPENAI_API_KEY = "your_openai_api_key"
```

4. **Run the bot**  
```bash
python main.py
```

---

## 🖼️ Example Output

![Example Video Output](https://github.com/dungangacore/tiktok-auto-generator/raw/main/output/output_video.gif)

---

## 📁 File Structure

```
.
├── main.py                 # Orchestrates the content creation workflow
├── config.py               # API keys (excluded from Git)
├── requirements.txt
├── .gitignore
├── src/
│   ├── content_generator.py    # Topic + script generator (GPT)
│   ├── text_to_speech.py       # ElevenLabs TTS
│   ├── video_creator.py        # Video composer using moviepy
│   └── link_shortener.py       # Monetized URL shortener
├── output/
│   └── output_video.mp4        # Example generated video
```

---

## 📄 License

This project is for **educational and non-commercial use only**.  
Use responsibly. No warranties provided.
