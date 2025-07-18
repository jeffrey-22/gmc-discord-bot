# Load tokens and keys from .env

import os
from dotenv import load_dotenv

load_dotenv()

discord_bot_token = os.getenv("DISCORD_BOT_TOKEN")
notion_authentication_token = os.getenv("NOTION_AUTHENTICATION_TOKEN")
notion_events_database_id = os.getenv("NOTION_EVENTS_DATABASE_ID")
notion_tasks_database_id = os.getenv("NOTION_TASKS_DATABASE_ID")
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")