import discord
from discord import ButtonStyle
from discord.commands import Option


bot = discord.Bot()
@bot.slash_command(
    integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },
)
async def say_hello(
        ctx: discord.ApplicationContext,
        message: Option(str, "Enter Message Content", required = True),
        amount: Option(int, "Enter the amount of times this will be repeated", required=True, min_value=1, max_value=6),
        attachment: Option(discord.Attachment, "Add any attachments", required=False)
):
    button = discord.ui.Button(label=f"Start", style=ButtonStyle.primary)
    amount = amount - 1
    async def button_callback(interaction):
        if attachment:
            file = await attachment.to_file()
            await interaction.response.send_message(message, file=file)
            for i in range(amount):
                file = await attachment.to_file()
                await interaction.followup.send(message, file=file)
        else:        
            await interaction.response.send_message(message)
            for i in range(amount):
                await interaction.followup.send(message)

    button.callback = button_callback
    view = discord.ui.View()
    view.add_item(button)

    # Send a message with the button
    await ctx.respond(f"Command is ready. Press the button below to spam your message", view=view, ephemeral=True)

bot.run("token")
