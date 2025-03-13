from flask import Flask, render_template, request, url_for
import os
from dotenv import load_dotenv
import requests
from webhook_sender import send_to_discord

load_dotenv()

API_TOKEN=os.getenv("CLOUDFLARE_API_TOKEN")
API_ID=os.getenv("CLOUDFLARE_API_ID")


app = Flask(__name__)

def generate_image(prompt):

    url = f"https://api.cloudflare.com/client/v4/accounts/{API_ID}/ai/run/"
    model = "@cf/lykon/dreamshaper-8-lcm"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {"prompt": prompt}
    
    response = requests.post(f"{url}{model}", headers=headers, json=data)
    if response.status_code == 200 and response.headers["Content-Type"] == "image/png":
        image_path = os.path.join("static", "generated.png")
        with open(image_path, "wb") as f:
            f.write(response.content)
        url = url_for("static", filename="generated.png")
    else:
        url = url_for("static", filename="fail.jpg")
    return url
    

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/send_webhook", methods=["POST"])
def send_webhook():
    text = request.form["text"]
    image_url = request.form["image_url"]
    if text and image_url:
        image_path = os.path.join("static", "generated.png")
    else:
        image_path = os.path.join("static", "fail.jpg")
    send_to_discord(image_path, text)
    return render_template("discord_response.html")
    

@app.route("/generate_card", methods=["POST"])
def generate_card():
    prompt = request.form["prompt"]
    message = request.form["message"]
    image_url = generate_image(prompt)
    return render_template("card.html", text=message, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)





