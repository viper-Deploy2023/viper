import os
import sys
import discord

from typing import List
from tinydb import TinyDB, Query

db = TinyDB("testdb.json")


class TestClient(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        # if message.content == "ping":
        cont = message.content
        match cont:
            case "ping":
                await message.channel.send("pong")


def is_question(question: str) -> bool:
    indicators: List[str] = [
        "?",
        "why",
        "what",
        "who",
        "whose",
        "which",
        "when",
        "where",
        "how",
    ]

    ret: bool = False
    for word in indicators:
        if word in question.lower():
            ret = True

    return ret


def get_env(name: str) -> str:
    VALUE: str = os.environ.get(name)

    if VALUE is None:
        raise ValueError(f"Environment variable '{name}' is not set.")

    return VALUE


def main() -> int:
    intents = discord.Intents.default()
    intents.message_content = True
    client = TestClient(intents=intents)
    client.run(get_env("DISCORD_TOKEN"))

    guid_name = client.guild

    return 0


if __name__ == "__main__":
    sys.exit(main())
