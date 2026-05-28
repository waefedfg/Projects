import discord

bot = discord.Bot()

# Use a placeholder for token for security reasons
token = "Put the tokennnnnn"

@bot.event
async def on_ready():
    print(f"{bot.user} is ready!!!!")

@bot.slash_command(name="hello", description="Says hello world!")
async def hello(ctx):
    await ctx.respond("Hello, World!")

bot.run(token)
