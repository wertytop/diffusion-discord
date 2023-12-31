import discord
import os
from dotenv import load_dotenv
import replicate
from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@tree.command(name="diffusion", description="gives a user an image generated by stable-diffusion")
async def diffusion(self, diffusionprompt: str, negativeprompts: str = None, outputs: int = None):
    await self.response.defer()

    if negativeprompts is None:
        negativeprompts = "None"

    if outputs is None:
        outputs = 1

    if outputs < 1:
        await self.followup.send("Too little outputs, you must be within `1-10`")
        return

    if outputs > 10:
        await self.followup.send("Too many outputs, you must be within `1-10`")
        return

    load_dotenv()
    replicate.Client(api_token=os.getenv("REPLICATE_API_TOKEN"))

    output = replicate.run(
        "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
        input={"prompt": diffusionprompt, "negative_prompt": negativeprompts, "num_outputs": outputs}

    )

    print(output[0])
    if outputs > 1:
        await self.followup.send(output[0])
        for i in range(outputs):
            await self.channel.send(output[i+1])
            print(i)
    else:
        await self.followup.send(output[0])

@tree.command(name="diffusion", description="gives a user an image generated by stable-diffusion",guild=discord.Object(id=1113884879252369438))
async def diffusion(self, diffusionprompt: str, negativeprompts: str = None, outputs: int = None):
    await self.response.defer()

    if negativeprompts is None:
        negativeprompts = "None"

    if outputs is None:
        outputs = 1

    if outputs < 1:
        await self.followup.send("Too little outputs, you must be within `1-10`")
        return

    if outputs > 10:
        await self.followup.send("Too many outputs, you must be within `1-10`")
        return

    load_dotenv()
    replicate.Client(api_token=os.getenv("REPLICATE_API_TOKEN"))

    output = replicate.run(
        "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
        input={"prompt": diffusionprompt, "negative_prompt": negativeprompts, "num_outputs": outputs}

    )

    print(output[0])
    if outputs > 1:
        await self.followup.send(output[0])
        for i in range(outputs):
            await self.channel.send(output[i+1])
            print(i)
    else:
        await self.followup.send(output[0])

@client.event
async def on_ready():
    print("Bot has booted!")
    await tree.sync(guild=discord.Object(id=1113884879252369438))


load_dotenv()
client.run(os.getenv("TOKEN"))
