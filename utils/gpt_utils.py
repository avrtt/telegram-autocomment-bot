import g4f
import os
from tenacity import retry, stop_after_attempt, wait_exponential
from config.config_loader import load_config

def load_prompt():
    prompt_path = os.path.join(os.path.dirname(__file__), '../config/prompt.txt')
    with open(prompt_path, 'r', encoding='utf-8') as file:
        return file.read()

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=4, max=30))
async def generate_comment(post_text, proxy_details):
    try:
        config = load_config()

        prompt_template = load_prompt()
        prompt = prompt_template.format(post_text=post_text)

        if config['Debug']['verbose'] == 'true':
            print(f"\n"
                f"----- BEGIN PROMPT -----\n" 
                f"{prompt + post_text}\n"
                f"----- END PROMPT -----\n")

        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[
                {
                    "role": "user",
                    "content": prompt + post_text
                }
            ],
            provider=g4f.Provider.Bing, # !!! replace with config['GPT']['provider']
            temperature=0.9,
            max_tokens=100,
            proxy=f"http://{proxy_details['login']}:{proxy_details['password']}@{proxy_details['ip']}:{proxy_details['port']}",
        )
        return response

    except Exception as e:
        print_red(f"Full error trace: {e}")
        raise RuntimeError(f"Error generating comment: {e}")