import random

class ContentGenerator:
    def generate(self) -> str:
        topics = [
            ("🧠 Psychology", "Why do people communicate silently in relationships?"),
            ("💬 Motivation", "A small habit every day builds massive success."),
            ("🎯 Entrepreneurship", "Wealth is created by solving problems."),
            ("💡 Interesting Facts", "Your brain decides before you are even aware."),
            ("👨‍⚕️ Health", "Drinking water after waking up boosts your metabolism."),
            ("🌌 Big Questions", "Some scientists believe reality might be a simulation.")
        ]
        topic, description = random.choice(topics)
        content = f"{topic} - Quick Insight:\n\nText: {description}"
        with open("content.txt", "w", encoding="utf-8") as f:
            f.write(content)
        return content
