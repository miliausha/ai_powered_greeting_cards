import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_to_discord(image_path, text):
     with open(image_path, "rb") as f:
        files = {
            "file": ("generated_image.jpeg", f)
        }
        data = {
            "payload_json": json.dumps({
                "content": text,
                "embeds": [
                    {
                        "title": "New card created",
                        "description": text,
                        "image": {
                            "url": "attachment://generated_image.jpeg"
                        }
                    }
                ]
            })
        }
        response = requests.post(DISCORD_WEBHOOK_URL, data=data, files=files)