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



async def fight(user, mob,interaction):
    while user.hp > 0 and mob.hp > 0:
        fight_embed, options = create_fight_embed(mob)
        view = discord.ui.View()
        for option in options:
            view.add_item(option)
        message = await interaction.response.send_message(embed=fight_embed,  view=view)

        options[0].callback = user.attack(mob)
        options[1].callback = user.use_inventory()
        options[2].callback = user.flee(mob)

        await mob.attack(user)