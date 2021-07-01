# Telegram Bot via Webhook (Flask)

Using Webhook method to setup Telegram Bot through Flask.

# Pre-requisite
- Python 3
- Flask
- Telegram
- Request
- Ngrok (optional)

Note: It is recommended to use `Ngrok` to speed up development prior to hosting it on Heroku or any cloud services.

# Getting Started
## Create a bot handle on Telegram and get your bot unique secret token.
1. Go to `@botfather` on Telegram to create a bot handle.
2. Type `/newbot` to create a new bot.
3. Name your bot e.g. EXAMPLE
4. Username of your bot e.g EXAMPLEBOT - This is the @username handle that can be search by users on Telegram
5. Once done, copy the token generated and add to the script `TOKEN` variable.

## Setup the script
1. Change `WEBHOOK_URL` to the hosting URL (this must be HTTPS).
2. Update Telegram by browsing to `{webook_url}/setwebhook` e.g. webhook_url = https://<url>/setwebhook/

## To enable bot for group chat
1. Go to `@botfather` on Telegram
2. Type `/mybot`, and select on your created bot e.g. EXAMPLEBOT
3. Go to 'Bot Settings' -> 'Group Privacy', and select on 'Turn off'

# Usage
After installing `Ngrok`, run `./ngrok http 5000` (with 5000 being the default port for Flask). 
`Ngrok` will return provide a publicly accessible URL for the running script, add the URL to the script `WEBHOOK_URL` variable.

Run `python3 bot.py` to start running and using the bot.