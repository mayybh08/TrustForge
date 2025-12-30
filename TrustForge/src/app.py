import os
import sys
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


@app.message(re.compile("(?i)hello|hi|hey|greet")) 
def message_greet(message, say):
    
    # Get the ID of the user who sent the message
    user_id = message['user']
    
    # Send a friendly greeting back to the user
    say(f"Hello <@{user_id}>! I am **TrustForge**. Your AI Security Agent is ready to help! 🚀")

# 1. Sabse pehle Project Root ka path nikalna (TrustForge folder)
# Ye line Python ko batayegi ki 'config' aur '.env' kahan hain
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# src/app.py mein load_dotenv ke upar ye add karein
env_path = os.path.join(BASE_DIR, ".env")
print(f"Looking for .env at: {env_path}")
print(f"Does .env exist there? {os.path.exists(env_path)}")

load_dotenv(env_path)

# 2. .env file ko absolute path se load karna
# Taaki terminal kahin bhi khula ho, .env mil jaye
load_dotenv(os.path.join(BASE_DIR, ".env"))

# 3. Connection check (Debug print - ise baad mein hata sakte hain)
token = os.getenv("SLACK_BOT_TOKEN")
if not token:
    print("❌ ERROR: SLACK_BOT_TOKEN nahi mila! .env file check karein.")
else:
    print(f"✅ Token detected: {token[:10]}...") # Sirf pehle 10 characters security ke liye

# 4. Ab connection logic
from config.db import get_db_connection

app = App(token=token)

# --- Baki ka code (hello message, commands) wahi rahega ---

# 3. Ek simple listener: Jab koi bot ko "hi" ya "hello" bole
@app.message("hello")
def message_hello(message, say):
    user = message['user']
    say(f"Namaste <@{user}>! Main hoon **TrustForge**. Aapka AI Agent taiyar hai! 🚀")

# 4. Database test karne ke liye command
@app.command("/dbcheck")
def db_check(ack, say):
    # Slack ko batana ki request mil gayi hai (must for commands)
    ack()
    
    conn = get_db_connection()
    if conn:
        say("TrustForge is connected to CockroachDB! ✅")
        conn.close()
    else:
        say("Database connection error. Check logs. ❌")

# 5. App start karne ka logic
if __name__ == "__main__":
    # SocketModeHandler app ko Slack se bina public URL ke connect karta hai
    handler = SocketModeHandler(app, os.getenv("SLACK_APP_TOKEN"))
    print("⚡ TrustForge is online and listening to Slack!")
    handler.start()