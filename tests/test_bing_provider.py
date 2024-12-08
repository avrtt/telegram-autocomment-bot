import asyncio
import g4f

async def test_bing_provider():
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default, # ensure you're using a supported model
            messages=[
                {"role": "user", "content": "Hello! How are you? Please respond briefly."}
            ],
            provider=g4f.Provider.Bing,
            temperature=0.7,
            max_tokens=50,
            proxy=None # replace with your proxy string if needed
        )
        print("Response:", response)
    except Exception as e:
        print("Error during Bing provider test:", e)

if __name__ == "__main__":
    asyncio.run(test_bing_provider())
