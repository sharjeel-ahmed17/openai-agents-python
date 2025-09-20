import asyncio

from agents import Agent, Runner

URL = "https://www.berkshirehathaway.com/letters/2024ltr.pdf"
from agentsdk_gemini_adapter import config


async def main():
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
    )

    result = await Runner.run(
        agent,
        [
            {
                "role": "user",
                "content": [{"type": "input_file", "file_url": URL}],
            },
            {
                "role": "user",
                "content": "Can you summarize the letter?",
            },
        ],
        run_config=config,
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
