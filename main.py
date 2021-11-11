from time import time

t = time()

import discord
from discord import Embed
from os import getenv
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.context import ComponentContext
from conjugations.ER import endings, verbs
from conjugations.IR import endings as irendings, verbs as irverbs
from conjugations.RE import endings as reendings, verbs as reverbs
from random import choice, shuffle
from dotenv import load_dotenv
from asyncio import TimeoutError

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
    random_verbs = verbs.copy()
    shuffle(random_verbs)
    random_endings = []
    embeds = []
    score = 0
    can_score = True
    for verb in random_verbs:
        e = choice(list(endings.keys()))
        random_ending = {e: endings[e]}
        random_endings.append(random_ending)
        embed = Embed(
            title=f"Conjugate {verb}", description=list(random_ending.keys())[0]
        )
        embeds.append(embed)
    start = time()
    for embed, ending, verb in zip(embeds, random_endings, random_verbs):
        await ctx.send(embed=embed)
        while True:
            try:
                msg = await bot.wait_for(
                    "message", check=lambda x: x.author == ctx.author, timeout=60
                )
                print(msg.content.lower()[-len(list(ending.values())[0]) :])
                if msg.content.lower()[
                    -len(list(ending.values())[0]) :
                ] in ending.values() and len(msg.content.lower()) == len(
                    verb
                ) - 2 + len(
                    list(ending.values())[0]
                ):
                    await msg.add_reaction("✅")
                    if can_score:
                        score += 1
                    can_score = True
                    break
                elif msg.content.lower() == "cancel":
                    await ctx.send("Cancelled!")
                    return
                else:
                    await msg.add_reaction("❌")
                    can_score = False
            except TimeoutError:
                await ctx.send("Timed out!")
                return
    end = time()
    await ctx.send(
        f"You got {score}/{len(random_verbs)}: {round(score/len(random_verbs)*100, 1)}%!\nYou took {round(end-start, 1)} seconds to complete!"
    )


@slash.subcommand(base="conjugate", name="ir", guild_ids=g)
async def conjugate_ir(ctx):
    random_verbs = irverbs.copy()
    shuffle(random_verbs)
    random_endings = []
    embeds = []
    score = 0
    can_score = True
    for verb in random_verbs:
        e = choice(list(irendings.keys()))
        random_ending = {e: irendings[e]}
        random_endings.append(random_ending)
        embed = Embed(
            title=f"Conjugate {verb}", description=list(random_ending.keys())[0]
        )
        embeds.append(embed)
    start = time()
    for embed, ending, verb in zip(embeds, random_endings, random_verbs):
        await ctx.send(embed=embed)
        while True:
            try:
                msg = await bot.wait_for(
                    "message", check=lambda x: x.author == ctx.author, timeout=60
                )
                print(msg.content.lower()[-len(list(ending.values())[0]) :])
                if msg.content.lower()[
                    -len(list(ending.values())[0]) :
                ] in ending.values() and len(msg.content.lower()) == len(
                    verb
                ) - 2 + len(
                    list(ending.values())[0]
                ):
                    await msg.add_reaction("✅")
                    if can_score:
                        score += 1
                    can_score = True
                    break
                elif msg.content.lower() == "cancel":
                    await ctx.send("Cancelled!")
                    return
                else:
                    await msg.add_reaction("❌")
                    can_score = False
            except TimeoutError:
                await ctx.send("Timed out!")
                return
    end = time()
    await ctx.send(
        f"You got {score}/{len(random_verbs)}: {round(score/len(random_verbs)*100, 1)}%!\nYou took {round(end-start, 1)} seconds to complete!"
    )


@slash.subcommand(base="conjugate", name="re", guild_ids=g)
async def conjugate_er(ctx):
    random_verbs = reverbs.copy()
    shuffle(random_verbs)
    random_endings = []
    embeds = []
    score = 0
    can_score = True
    for verb in random_verbs:
        e = choice(list(reendings.keys()))
        random_ending = {e: reendings[e]}
        random_endings.append(random_ending)
        embed = Embed(
            title=f"Conjugate {verb}", description=list(random_ending.keys())[0]
        )
        embeds.append(embed)
    start = time()
    for embed, ending, verb in zip(embeds, random_endings, random_verbs):
        await ctx.send(embed=embed)
        while True:
            try:
                msg = await bot.wait_for(
                    "message", check=lambda x: x.author == ctx.author, timeout=60
                )
                print(msg.content.lower()[-len(list(ending.values())[0]) :])
                if (
                    msg.content.lower()[-len(list(ending.values())[0]) :]
                    in ending.values()
                    and len(msg.content.lower())
                    == len(verb) - 2 + len(list(ending.values())[0])
                ) or (
                    list(ending.values())[0] == ""
                    and msg.content.lower() == verb.replace("re", "")
                ):
                    await msg.add_reaction("✅")
                    if can_score:
                        score += 1
                    can_score = True
                    break
                elif msg.content.lower() == "cancel":
                    await ctx.send("Cancelled!")
                    return
                else:
                    await msg.add_reaction("❌")
                    can_score = False
            except TimeoutError:
                await ctx.send("Timed out!")
                return
    end = time()
    await ctx.send(
        f"You got {score}/{len(random_verbs)}: {round(score/len(random_verbs)*100, 1)}%!\nYou took {round(end-start, 1)} seconds to complete!"
    )


keep_alive()
bot.load_extension("jishaku")
bot.run(getenv("TOKEN"))
