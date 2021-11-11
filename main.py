from time import time

t = time()

from os import getenv
from discord.ext import commands
from discord_slash import SlashCommand
from conjugations.ER import er_conjugate
from conjugations.IR import ir_conjugate
from conjugations.RE import re_conjugate
from dotenv import load_dotenv

from keep_alive import keep_alive

load_dotenv()

bot = commands.Bot(command_prefix="fkjwahkjfan", help_command=None)
slash = SlashCommand(bot, sync_commands=True, delete_from_unused_guilds=True)
g = [908159929662193706]


@bot.event
async def on_ready():
    print("Ready!")
    t2 = time()
    t3 = t2 - t
    print(f"{t3} seconds")


@slash.subcommand(base="conjugate", name="er", guild_ids=g)
async def conjugate_er(ctx):
    await er_conjugate(ctx, bot)


@slash.subcommand(base="conjugate", name="ir", guild_ids=g)
async def conjugate_ir(ctx):
    await ir_conjugate(ctx, bot)


@slash.subcommand(base="conjugate", name="re", guild_ids=g)
async def conjugate_re(ctx):
    await re_conjugate(ctx, bot)


keep_alive()
bot.load_extension("jishaku")
bot.run(getenv("TOKEN"))
