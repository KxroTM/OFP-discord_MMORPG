import discord

Embeds = {
    "spawn": discord.Embed(
        title="*...*", 
        color=0x055a28
    ).set_image(url="https://c.tenor.com/zEhLVzv0HSoAAAAC/tenor.gif"),
    "1" : discord.Embed(
        title="*un couteau ...?*", 
        color=0x055a28
    ).set_image(url="https://cdn.discordapp.com/attachments/1297290803244171336/1297290834374561823/DALLE_2024-10-19_22.10.02_-_A_top-down_anime-style_view_of_a_scene_where_a_person_is_looking_down_at_their_bag_on_the_ground_which_has_fallen_on_the_grass_at_night._The_person_c.webp?ex=671563bd&is=6714123d&hm=3ba83baf64da998e27e02ef9558966980f81457ab1447c0ed923858954bb3af5&"),
    "2" : discord.Embed(
        title="*je ne vois rien ... \nOù suis-je ... ?*", 
        color=0x055a28
    ).set_image(url="https://c.tenor.com/dLhz9mUgq9EAAAAd/tenor.gif"),
    "3" : discord.Embed(
        title="*... Qu'est ce .. que .. c'est ... je .. dois ... fuir !*", 
        color=0x055a28
    ).set_image(url="https://c.tenor.com/EOlZo1vc8lcAAAAC/tenor.gif"),
    "4" : discord.Embed(
        title="*.. Cette chose m'a rattraper .. je dois .. me défendre *", 
        color=0x055a28
    ),
    "starting_fight" : discord.Embed(
        title="**Survie : **", 
        color=0x055a28
    ).set_image(url="https://cdn.discordapp.com/attachments/897579462772785152/1297302036135809045/file-g5HLYMgzN7jL0lmtmgVOqNc1.png?ex=67156e2c&is=67141cac&hm=364f20ac9aa7387bc96e9d7c753a87e7a022768b344f77abec3b0ed04b509fd4&"),

}

Options = {
    "spawn": [
        discord.ui.Button(label="...", style=discord.ButtonStyle.green, custom_id="option_1"),
    ],
    "1": [
        discord.ui.Button(label="Ramasser", style=discord.ButtonStyle.green, custom_id="option_1")
    ],
    "2": [
        discord.ui.Button(label="Avancer", style=discord.ButtonStyle.green, custom_id="option_1"),
    ],
    "3": [
        discord.ui.Button(label="Fuir", style=discord.ButtonStyle.green, custom_id="option_1"),
    ],
    "4": [
        discord.ui.Button(label="Sortir le couteau", style=discord.ButtonStyle.green, custom_id="option_1"),
    ],
    "starting_fight": [
        discord.ui.Button(label="Commencer le combat", style=discord.ButtonStyle.green, custom_id="option_1"),
    ],
}

