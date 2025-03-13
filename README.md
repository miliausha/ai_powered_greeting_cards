# ai_powered_greeting_cards

This project is a Flask web application that allows users to create and generate digital cards. The application uses the Cloudflare text-to-image API to generate images based on user prompts and sends the generated cards to Discord. Model used in this app is @cf/lykon/dreamshaper-8-lcm . More information about models you can find here: https://cloudflare.com

This is educational Workshop for 42Bangkok students  to learn how to interact with AI and Discord

## Features

- Generate images based on user prompts using the Cloudflare text-to-image API.
- Create digital cards with custom messages.
- Send generated cards to Discord.

## Requirements

- Python 3.8+
- Account on Cloudflare.com

## Installation

1. Clone the repository:

```bash
git clone https://github.com/miliausha/ai_powered_greeting_cards.git
cd ai_powered_greeting_cards

```

2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source  venv/bin/activate
```

3. Install the reqiored packages:

```bash
pip install -r requirements.txt
```

## Configuration

Create a .env file in the root directory
Create account on cloudflare.com
add your Cloudflare API token and account ID and Discord webhook URL:

CLOUDFLARE_API_TOKEN=your_cloudflare_api_token
CLOUDFLARE_API_ID=your_cloudflare_account_id
DISCORD_WEBHOOK_URL=your_discord_webhook_url
