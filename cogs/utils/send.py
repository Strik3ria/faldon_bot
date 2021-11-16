from cogs.utils.codify import codify


async def send(ctx, response):
    return await ctx.channel.send(codify(response))
