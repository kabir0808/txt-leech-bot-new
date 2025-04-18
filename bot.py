from flask import Flask
import os
from telegram.ext import Updater

app = Flask(__name__)

@app.route('/health')
def health():
    return "OK"

def run_bot():
    updater = Updater(os.getenv("TELEGRAM_TOKEN"), use_context=True)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    import threading
    threading.Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 8080)))
