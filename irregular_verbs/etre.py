from asyncio import TimeoutError
from discord import Embed
from random import shuffle
from time import time

verbs = {
    "je": "suis",
    "tu": "es",
    "il/elle/on": "est",
    "nous": "sommes",
    "vous": ("êtes", "etes"),
    "ils/elles": "sont",
}


async def use_etre(ctx, bot):
    random_verbs = list(verbs.copy().keys())
    shuffle(random_verbs)
    embeds = []
    can_score = True
    score = 0
    for verb in random_verbs:
        embed = Embed(title="Être", description=f"{verb.capitalize()} (être)")
        embeds.append(embed)
    start = time()
    for verb, embed in zip(random_verbs, embeds):
        await ctx.send(embed=embed)
        while True:
            try:
                msg = await bot.wait_for(
                    "message", check=lambda m: m.author == ctx.author, timeout=60
                )
                if msg.content.lower() == verbs[verb]:
                    await msg.add_reaction("✅")
                    if can_score:
                        score += 1
                    else:
                        can_score = True
                    break
                elif msg.content.lower() == "cancel":
                    await ctx.send("Cancelled!")
                    return
                elif verb == "vous" and msg.content.lower() in verbs[verb]:
                    await msg.add_reaction("✅")
                    if can_score:
                        score += 1
                    else:
                        can_score = True
                    break
                else:
                    await msg.add_reaction("❌")
                    can_score = False
            except TimeoutError:
                await ctx.send("Timed out!")
                return
    end = time()
    await ctx.send(
        f"You got {score}/{len(random_verbs)}: {round(score / len(random_verbs) * 100, 1)}%!\nYou took {round(end - start, 1)} seconds to complete!"
    )
