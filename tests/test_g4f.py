import asyncio
import g4f

async def test_g4f():
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[
                {"role": "user", "content": "Hello, test the API."}
            ],
            provider=g4f.Provider.Bing,
            temperature=0.7,
            max_tokens=50
        )
        print("API Response:", response)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    asyncio.run(test_g4f())
