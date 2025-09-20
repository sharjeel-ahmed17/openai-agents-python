import asyncio

from agents import Agent, Runner

URL = "https://upload.wikimedia.org/wikipedia/commons/0/0c/GoldenGateBridge-001.jpg"
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
                "content": [{"type": "input_image", "detail": "auto", "image_url": URL}],
            },
            {
                "role": "user",
                "content": "What do you see in this image?",
            },
        ],
        run_config=config,
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
