@client.event
@commands.has_role('papa throw')
async def on_message(message):
  if message.author.bot:
       return
  if message.content != "":
    if y == 0 or y2 == 0 or y3 == 0: 
      await message.channel.send(f"{message.author.mention} papa throw")