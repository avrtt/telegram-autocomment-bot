from telethon import TelegramClient
from telethon.events import NewMessage
from telethon.tl.functions.channels import JoinChannelRequest
from utils.log_utils import print_green, print_red
from bot.event_handlers import handle_new_posts
import asyncio

async def start_bot(config):
    api_id = config['Telegram']['api_id']
    api_hash = config['Telegram']['api_hash']
    device_model = config['Telegram']['device_model']
    system_version = config['Telegram']['system_version']
    auto_join = config['Telegram']['auto_join'].lower() == "true"
    channel_usernames = [ch.strip() for ch in config['Telegram']['channel_usernames'].split(",")]
    proxy_details = {
        "login": config['Telegram']['proxy_login'],
        "password": config['Telegram']['proxy_password'],
        "ip": config['Telegram']['proxy_ip'],
        "port": config['Telegram']['proxy_port'],
    }

    client = TelegramClient(
        'bot_session', api_id, api_hash, device_model=device_model, system_version=system_version
    )
    
    commented_messages = {}

    async with client:
        print_green(f"Bot started as {await client.get_me()}.")

        if auto_join:
            for username in channel_usernames:
                try:
                    await client(JoinChannelRequest(username))
                    print_green(f"Joined channel: @{username}")
                except Exception as e:
                    print_red(f"Failed to join @{username}: {e}")

        channel_entities = [await client.get_entity(username) for username in channel_usernames]
        for entity in channel_entities:
            commented_messages[entity.id] = set()
            client.add_event_handler(
                lambda e: handle_new_posts(e, client, commented_messages, proxy_details),
                event=NewMessage(incoming=True, chats=entity)
            )

        await client.run_until_disconnected()
