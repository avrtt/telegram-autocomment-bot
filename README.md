Here you can find a Python app that allows you to monitor for new posts to instantly send a comment once published, using Telegram bot-like functionality. You can specify the list of channels to monitor, as well as the behavior (prompt) to generate comments according to.  

Developed with [Telethon](https://github.com/LonamiWebs/Telethon), [gpt4free](https://github.com/xtekky/gpt4free) and [Tenacity](https://github.com/jd/tenacity). No OpenAI account required.

This is a public part of my **freelance** project. Need services? Check out **[my website](https://avrtt.github.io/freelance)** 👈👀.   

## Notice
Absolutely no way you should use such software for spamming. Telegram moderation will ban your account after a few reports from other users. Use in your own channels for fun and to get familiar with the technology. 

## Structure

```
telegram-autocomment-bot/
│
├── config/
│   ├── settings.ini
│   └── config_loader.py
│
├── utils/
│   ├── gpt_utils.py
│   ├── log_utils.py
│
├── bot/
│   ├── bot_logic.py (core functionality)
│   ├── event_handlers.py
│
├── requirements.txt
└── start.py
```

## Installation
1. Clone and navigate to the repository:
    ```
    git clone git@github.com:avrtt/telegram-autocomment-bot.git
    cd telegram-autocomment-bot
    ```

2. Since using virtual environments is a good practice, I highly recommend you to create one:
    ```
    python3 -m venv venv
    ```

    Then activate the virtual environment:
    - On Linux/macOS:
        ```
        source venv/bin/activate
        ```
    - On Windows:
        ```
        venv\Scripts\activate
        ```

3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Create a `config/settings.ini` file with the following content:
    ```
    [Telegram]
    api_id = <your_api_id*>
    api_hash = <your_api_hash*>
    channel_usernames = <channel1, channel2, ...>
    auto_join = <true/false>

    # optional
    device_model =
    system_version =
    proxy_login =
    proxy_password =
    proxy_ip =
    proxy_port =
    ```
    \* Get your Telegram API ID and hash [here](https://my.telegram.org/auth). You should log in using the phone number of the bot account, navigate to "API development tools" and create a new application. **Keep them secret!**

5. Run:
    ```
    python start.py
    ```

6. Once prompted, provide Telethon with the same phone number you entered when created the API. You'll receive a code again.

7. If your account has two-step verification enabled, Telethon will prompt you for a password.

<br>

Now, if you go into **Active sessions** in your bot account, you will see the new device you just registered. Have fun!

## Contrubition
Feel free to open PRs and issues.

## License
MIT
