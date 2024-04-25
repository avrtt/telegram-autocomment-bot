from config.config_loader import load_config
from bot.bot_logic import start_bot
import asyncio

if __name__ == "__main__":
    config = load_config()
    asyncio.run(start_bot(config))
