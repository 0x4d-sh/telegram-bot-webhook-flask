from flask import Flask, request
import requests
import telegram

# Config
TOKEN = "<number>:<alphanumeric>"
TELEGRAM_URL = "https://api.telegram.org/bot{token}".format(token=TOKEN)
WEBHOOK_URL  = "https://<url>"

# To retrieve unique user chat ID and group ID, use @IDBot
WHITELISTED_USERS = []
bot = telegram.Bot(token=TOKEN)

# Bot
app = Flask(__name__)

def sendmessage(chat_id):
    # As the bot is searchable and visble by public.
    # Limit the response of bot to only specific chat IDs.
    authorised = True if chat_id in WHITELISTED_USERS else False
                
    message = "<Notification>"

    if not authorised:
        message = "You're not authorised."

    url = "{telegram_url}/sendMessage".format(telegram_url=TELEGRAM_URL)
    payload = {
        "text": message,
        "chat_id": chat_id
        }
    
    resp = requests.get(url,params=payload)

@app.route("/", methods=["POST","GET"])
def index():
    if(request.method == "POST"):
        response = request.get_json()
        
        # To Debug
        # print(response)

        # To run only if 'message' exist in response.
        if 'message' in response:

            # To not response to other bots in the same group chat
            if 'entities' not in response['message']:
            
                chat_id = response["message"]["chat"]["id"]
                sendmessage(chat_id)

    return "Success"

@app.route("/setwebhook/")
def setwebhook():
    s = requests.get("{telegram_url}/setWebhook?url={webhook_url}".format(telegram_url=TELEGRAM_URL,webhook_url=WEBHOOK_URL))
  
    if s:
        return "Success"
    else:
        return "Fail"

if __name__ == "__main__":
    app.run(debug=True)