from hata import Client, IntentFlag, wait_for_interruption

from .bot import bladelist_bot


@bladelist_bot.events
async def ready(client):
    print("{client.name} Ready!")


if __name__ == "__main__":
    # Start the bot
    bladelist_bot.start()

    # Disconnect your bot when keyboard interrupt is received
    wait_for_interruption()
