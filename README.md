**🇺🇸 English** &nbsp; • &nbsp; **[🇷🇺 Русский](https://github.com/avrtt/telegram-autocomment-bot/blob/main/README_ru.md)**

<br>

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
│   ├── prompt.txt
│   └── config_loader.py
│
├── utils/
│   ├── gpt_utils.py
│   └── log_utils.py
│
├── bot/
│   ├── bot_logic.py (core functionality)
│   └── event_handlers.py
│
├── tests/
│   ├── test_g4f.py
│   └── test_bing_provider.py
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
    auto_join = true
    channel_usernames = <channel1, channel2, ... **>

    [GPT]
    provider = Bing

    [Debug]
    verbose = false

    [Proxy] # optional
    proxy_login =
    proxy_password =
    proxy_ip =
    proxy_port =

    [Metadata] # optional
    device_model =
    system_version =
    ```
    \* Get your Telegram API ID and hash [here](https://my.telegram.org/auth). You should log in using the phone number of the bot account, navigate to "API development tools" and create a new application. **Keep them secret!**  
    \** Specify channels without the `@` symbol. Your private channels won't work.

5. Run:
    ```
    python start.py
    ```

6. Once prompted, provide Telethon with the same phone number you entered when created the API. You'll receive a code again.

7. If your account has two-step verification enabled, Telethon will prompt you for a password as well.

<br>

Now, if you go into **Active sessions** in your bot account, you will see the new device you just registered. Have fun!

## Configuration
### Behavior
The first thing you'd probably want to configure is a prompt that sets the bot's behavior. You can write your prompt in the `prompt.txt` file. Here it's simple: use the bot as if it were ChatGPT. 

It's recommended to describe the behavior in the language you want the bot to write in. 

Add something like `Comment on the following text:` at the end of the prompt, since the publication text gets inserted after the prompt in the code.

### Settings
Here's the detailed description of variables in the `settings.ini` file (default values are <ins>underscored</ins>):  

- `auto_join`: Whether the bot should join channels at the beginning of the session **(<ins>true</ins>/false)**  
- `provider`: Which model provider to use **(<ins>Bing</ins>, Liaobots, Phind, etc.)**  
- `verbose`: Turn on the verbose debugging mode that shows connection trace, full prompt texts and other info in your console **(true/<ins>false</ins>)**  

## Testing & troubleshooting
### Testing provider connection
Run the isolated script for g4f:
```
python tests/test_g4f.py
```

You will likely get `Error: Bing is not working`, so run the isolated script for Bing to ensure:
```
python tests/test_bing_provider.py
```

If Bing isn't working, try to change provider or use proxy.

### My ISP has blocked Bing/OpenAI
If you can't access such services without a VPN, then ~~you're probably from Russia~~ you could try using a proxy. Or, maybe, use a system-wide VPN, DPI bypass utilities, etc. Try [GreenTunnel](https://github.com/SadeghHayeri/GreenTunnel).

### Using different providers
The full list of providers and their compatibility with models are listed in the [g4f repository](https://github.com/techwithanirudh/g4f).

## To do
- Replace `Bing` with `config['GPT']['verbose']` in `gpt_utils.py`
- Add more tweaks
- Add unit tests

## Contrubition
Feel free to open PRs and issues.

## License
MIT
