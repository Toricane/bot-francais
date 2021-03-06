from asyncio import TimeoutError
from discord import Embed
from random import choice, shuffle
from time import time

endings = {
    "je": "e",
    "tu": "es",
    "il/elle/on": "e",
    "nous": "ons",
    "vous": "ez",
    "ils/elles": "ent",
}

verbs = ["parler", "téléphoner", "aimer", "acheter", "écouter", "regarder"]


async def er_conjugate(ctx, bot):
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
            title=f"Conjugate {verb}",
            description=f"{list(random_ending.keys())[0].capitalize()} ({verb})",
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
        f"You got {score}/{len(random_verbs)}: {round(score / len(random_verbs) * 100, 1)}%!\nYou took {round(end - start, 1)} seconds to complete!"
    )
