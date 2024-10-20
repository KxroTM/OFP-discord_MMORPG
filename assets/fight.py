import discord


def create_fight_embed(mob):
    fight_embed = discord.Embed(
        title="**Survie : **",
        description=f"**{mob.name}** vous attaque !", 
        color=0x055a28
    ).set_image(url=mob.image).set_footer(text='"a" pour attaquer, "i" pour ouvrir l\'inventaire, "f" pour fuir')

    return fight_embed



async def fight(user, mob,channel,client):
    while user.hp > 0 and mob.hp > 0:
        fight_embed = create_fight_embed(mob)
        await channel.send(embed=fight_embed)
        def check(m):
            return m.author == user and (m.content.lower() == 'a' or m.content.lower() == 'i' or m.content.lower() == 'f')
        msg = await client.wait_for('message', check=check)

        if msg.content == 'a':
            user.attack(mob)
        elif msg.content == 'i':
            await user.open_inventory(channel)
        elif msg.content == 'f':
            if await user.flee(mob):
                await channel.send("Vous avez fui le combat")
                break
            else:
                await channel.send("Vous n'avez pas réussi à fuir")

        mob.attack(user)