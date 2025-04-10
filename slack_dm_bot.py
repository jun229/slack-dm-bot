from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
import os
import time

# Load .env.local
load_dotenv(dotenv_path=".env.local")

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
CHANNEL_IDS = (os.getenv("CHANNEL_ID")).split(",")
MESSAGE = os.getenv("MESSAGE")

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

def get_channel_members(CHANNEL_ID):
    try:
        result = client.conversations_members(channel=CHANNEL_ID)
        return result["members"]
    except SlackApiError as e:
        print(f"Error fetching channel members: {e}")
        return []


def send_dm(user_id, message):
    try:
        client.chat_postMessage(channel=user_id, text=message)
        print(f"Message sent to {user_id}")
    except SlackApiError as e:
        print(f"Error sending message to {user_id}: {e}")

if __name__ == "__main__":
    all_users = get_user_ids()
    channel_users = []
    for CHANNEL_ID in CHANNEL_IDS:
        channel_users += get_channel_members(CHANNEL_ID)
    users = [user_id for user_id in all_users if user_id in channel_users]
    users = set(users)
    for user_id in users:
        send_dm(user_id, MESSAGE)
        time.sleep(1.5)