import os

import discord
from discord import app_commands
from dotenv import load_dotenv

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@tree.command(name='ping', description="Replies with pong!")
async def ping_command(interaction):
    await interaction.response.send_message(content="Pong!", ephemeral=True)


async def register_commands():
    print("Registering commands...")
    commands = await tree.sync()
    print(f"Registered {len(commands)} commands")


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    await register_commands()

load_dotenv()
TOKEN = os.getenv("TOKEN")
client.run(TOKEN)
