

import discord
import os

access_token = os.environ["BOT_TOKEN"]
client = discord.Client()


@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game("인증봇"))
  print("원진#7917") 
  print(client.user.name) 
  print(client.user.id) 
   
@client.event
async def on_message(message):
 
  if message.content.startswith('/인증'): 
    author = message.guild.get_member(int(message.author.id))
    role = discord.utils.get(message.guild.roles, name="손님") 
    await author.add_roles(role)
    await message.channel.send(embed=embed)


embed=discord.Embed(title="인증", description="완료되었습니다.", color=0x8c44d8)







  
client.run(access_token)