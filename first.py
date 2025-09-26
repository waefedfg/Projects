import discord

bot = discord.Bot()

# Use a placeholder for token for security reasons
token = "MTA0NjU1MjM5Mzc0OTM3NzA4Ng.GXV207.zIirYDvfd49mtFpbA_2jA_7_3m-XqS6sPaSfdE"

@bot.event
async def on_ready():
    print(f"{bot.user} is ready!!!!")

@bot.slash_command(name="hello", description="Says hello world!")
async def hello(ctx):
    await ctx.respond("Hello, World!")

bot.run(token)
