from config.config_loader import load_config
from bot.bot_logic import start_bot
import asyncio
import logging

if __name__ == "__main__":
    config = load_config()

    if config['Debug']['verbose'] == 'true':
        logging.basicConfig(level=logging.DEBUG)

    asyncio.run(start_bot(config))
