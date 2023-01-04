import discord
from discord.utils import get
from discord.ext.commands import Bot
from config import TOKEN, ROLE_NAME, REMOVE_ROLE

bot = Bot(command_prefix="*", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Now logged in as {0.user}'.format(bot))  
   
@bot.event
async def on_voice_state_update(member, before, after):
    guild = member.guild

    if not get(guild.roles, name=ROLE_NAME): # Create role name if it doesnt exist
        await guild.create_role(name=ROLE_NAME)

    if after.channel is None:

        await member.remove_roles(discord.utils.get(member.guild.roles, name=ROLE_NAME))
        await member.add_roles(discord.utils.get(member.guild.roles, name=REMOVE_ROLE))


    elif not before.channel and after.channel:

        await member.add_roles(discord.utils.get(member.guild.roles, name=ROLE_NAME))
        await member.remove_roles(discord.utils.get(member.guild.roles, name=REMOVE_ROLE))

bot.run(TOKEN)