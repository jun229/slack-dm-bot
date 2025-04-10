from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
import os

# Load .env.local
load_dotenv(dotenv_path=".env.local")

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
MESSAGE = "Hey! Please take 1 min to fill out this form: [your-form-link]"

client = WebClient(token=SLACK_BOT_TOKEN)

def get_user_ids():
    user_ids = []
    try:
        result = client.users_list()
        for member in result['members']:
            if not member['is_bot'] and not member['deleted']:
                user_ids.append(member['id'])
    except SlackApiError as e:
        print(f"Error fetching users: {e}")
    return user_ids

def send_dm(user_id, message):
    try:
        client.chat_postMessage(channel=user_id, text=message)
        print(f"Message sent to {user_id}")
    except SlackApiError as e:
        print(f"Error sending message to {user_id}: {e}")

if __name__ == "__main__":
    users = get_user_ids()
    for user_id in users:
        send_dm(user_id, MESSAGE)
