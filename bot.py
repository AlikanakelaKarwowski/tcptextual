import twitchio
from twitchio.ext import commands
import os

from twitchio.ext.commands.core import Context

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

@bot.command(name="create")
async def create(ctx: commands.Context, command_name:str, output:str) ->None:
    await create_command(command_name, output)
    await ctx.send(f"Command {command_name} created")


async def create_command(command_name:str, output:str) ->None:
    async def new_command(ctx: commands.Context) -> None:
        await ctx.send(f"{output} success")
        
    bot.add_command(commands.Command(command_name,(new_command)))


bot.run()
