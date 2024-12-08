from utils.gpt_utils import generate_comment
from utils.log_utils import print_green, print_red
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import ChannelPrivateError
import asyncio

async def handle_new_posts(event, client, commented_messages, proxy_details):
    message = event.message
    channel_id = message.peer_id.channel_id

    if channel_id in commented_messages and message.id not in commented_messages[channel_id]:
        try:
            comment_text = await generate_comment(message.text, proxy_details)
            await client.send_message(entity=event.chat, message=comment_text, comment_to=message)
            print_green("Comment successfully posted.")
            commented_messages[channel_id].add(message.id)
            
        except ChannelPrivateError as e:
            print_red(f"ChannelPrivateError: {e}")

        except Exception as e:
            print_red(f"Error commenting: {e}")
