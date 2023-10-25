import json
import os

import twitchio
from twitchio.ext import commands
from twitchio.ext.commands.core import Context

from config_generator import Controller_Config


class TCPTextualBot(commands.Bot):
    async def event_command_error(self, context: Context, error: Exception) -> None:
        if isinstance(error, commands.CommandNotFound):
            return
        if isinstance(error, commands.ArgumentParsingFailed):
            await context.send(error.message)
            return
        if isinstance(error, commands.MissingRequiredArgument):
            await context.send("Your missing part of the arguement: " + error.name)
            return
        if isinstance(error, commands.CheckFailure):
            await context.send(error.message)
            return
        else:
            print(error)

bot = TCPTextualBot(token=os.environ.get("ACCESS_TOKEN"),
            prefix='!',
            nick=os.environ.get("BOT_NICK"),
            initial_channels=[os.environ.get("CHANNEL")])

@bot.command(name="loadCmds")
async def load_commands(ctx: commands.Context) ->None:
    await load_config("test", "config")
    await ctx.send(f"Commands created")


async def create_command(command_name:str, keys:list[str], duration:float, cooldown:float | None, chance:float | None) ->None:
    async def new_command(ctx: commands.Context) -> None:
        await ctx.send(f"{command_name} | {keys} | {duration} | {cooldown} | {chance} success")
        
    bot.add_command(commands.Command(command_name,(new_command)))

async def load_config(file:str, path:str|None):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, path, f"{file}.json")
    with open(file_path, 'r') as f:
        json_data = json.load(f)
    configs = [Controller_Config(**config) for config in json_data]
    for config in configs:
        await create_command(config.command_name, config.keys, config.duration, config.cooldown, config.chance)


bot.run()
