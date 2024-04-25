import g4f
from tenacity import retry, stop_after_attempt

@retry(stop=stop_after_attempt(5))
async def generate_comment(post_text, proxy_details):
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"You're a casual Telegram user. React briefly and emotionally to this post. "
                        f"Keep your comment sarcastic, concise, witty, and no longer than 15 words: \n\n"
                        f"`{post_text}`"
                    )
                }
            ],
            provider=g4f.Provider.Bing,
            temperature=0.9,
            max_tokens=100,
            proxy=f"http://{proxy_details['login']}:{proxy_details['password']}@{proxy_details['ip']}:{proxy_details['port']}",
        )
        return response
    except Exception as e:
        raise RuntimeError(f"Error generating comment: {e}")
