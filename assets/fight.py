import discord


def create_fight_embed(mob):
    fight_embed = discord.Embed(
        title="**Survie : **",
        description=f"**{mob.name}** vous attaque !", 
        color=0x055a28
    ).set_image(url=mob.image)

    options = [
        discord.ui.Button(label="Attaquer", style=discord.ButtonStyle.green, custom_id="option_1"),
        discord.ui.Button(label="Inventaire", style=discord.ButtonStyle.green, custom_id="option_2"),
        discord.ui.Button(label="Fuir", style=discord.ButtonStyle.red, custom_id="option_3"),
    ]

    return fight_embed, options



async def fight_callback(interaction: discord.Interaction, mob):
    choice = interaction.custom_id
    if choice == "option_1":
        await interaction.response.send_message("Vous avez choisi d'attaquer !", ephemeral=True)
    elif choice == "option_2":
        await interaction.response.send_message("Vous avez choisi d'ouvrir votre inventaire !", ephemeral=True)
    elif choice == "option_3":
        await interaction.response.send_message("Vous avez choisi de fuir !", ephemeral=True)
    else:
        await interaction.response.send_message("Vous avez choisi de ne rien faire !", ephemeral=True)
    return
