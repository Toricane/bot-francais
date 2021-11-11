from asyncio import TimeoutError
from discord import Embed
from random import shuffle
from time import time

qa = {
    "quand": "when",
    "qui": "who",
    "que": "what",
    "quel/quelle": "which",
    "pourquoi": "why",
    "où": "where",
    "comment": "how",
    "combien": ("how many", "how much"),
}
aq = {
    "when": ("quand",),
    "who": ("qui",),
    "what": ("que",),
    "which": ("quel", "quelle"),
    "why": ("pourquoi",),
    "where": ("ou", "où"),
}


async def get_ans(ctx, bot):
    random_qs = list(qa.copy().keys())
    shuffle(random_qs)
    embeds = []
    can_score = True
    score = 0
    for q in random_qs:
        embed = Embed(title=q.capitalize(), description=f"What does {q} mean?")
        embeds.append(embed)
    start = time()
    for q, embed in zip(random_qs, embeds):
        await ctx.send(embed=embed)
        while True:
            try:
                msg = await bot.wait_for(
                    "message", check=lambda m: m.author == ctx.author, timeout=60
                )
                if msg.content.lower() == qa[q]:
                    await msg.add_reaction("✅")
                    if can_score:
                        score += 1
                    else:
                        can_score = True
                    break
                elif msg.content.lower() == "cancel":
                    await ctx.send("Cancelled!")
                    return
                elif q == "combien" and msg.content.lower() in qa[q]:
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
        f"You got {score}/{len(random_qs)}: {round(score / len(random_qs) * 100, 1)}%!\nYou took {round(end - start, 1)} seconds to complete!"
    )


async def get_ques(ctx, bot):
    random_as = list(aq.copy().keys())
    shuffle(random_as)
    embeds = []
    can_score = True
    score = 0
    for a in random_as:
        embed = Embed(
            title=a.capitalize(), description=f"What does {a} mean in French?"
        )
        embeds.append(embed)
    start = time()
    for a, embed in zip(random_as, embeds):
        await ctx.send(embed=embed)
        while True:
            try:
                msg = await bot.wait_for(
                    "message", check=lambda m: m.author == ctx.author, timeout=60
                )
                if msg.content.lower() in aq[a]:
                    await msg.add_reaction("✅")
                    if can_score:
                        score += 1
                    else:
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
        f"You got {score}/{len(random_as)}: {round(score / len(random_as) * 100, 1)}%!\nYou took {round(end - start, 1)} seconds to complete!"
    )
