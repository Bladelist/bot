from hata import Client, IntentFlag

from .config import BOT_TOKEN

bladelist_bot = Client(
    BOT_TOKEN,
    intents=IntentFlag().update_by_keys(
        guild_users=False, guild_presences=False, message_content=False
    ),
)
