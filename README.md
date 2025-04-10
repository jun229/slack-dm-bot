# Slack DM Bot 🤖

This Python bot sends a private DM to every real member in one or more specified Slack channels — perfect for club announcements, form reminders, and more.

---

## 🔧 Setup

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/slack-dm-bot.git
cd slack-dm-bot
```

### 2. Install Dependencies

```bash
pip install slack_sdk
pip install python-dotenv
```

### 3. Create and Edit Your .env.local File

Here is the .env.local template:

```bash
SLACK_BOT_TOKEN={Your API key}
CHANNEL_ID={Your Slack channel IDs. You can add multiple channels seperated by commas i.e "C1234,C4321"}
MESSAGE="{Your message}"
```

### 4. Running the Script

Run this command in your terminal

```bash
python slack_dm_bot.py
```
