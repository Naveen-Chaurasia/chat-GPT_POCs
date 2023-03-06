import asyncio
from chatgpt_wrapper import AsyncChatGPT

async def main():
    agpt = AsyncChatGPT()
    await agpt.create()
    await agpt.refresh_session()
    response = await agpt.ask("Hello, world!")
    print(response)
    # Hello there! How can I assist you today?

asyncio.run(main())