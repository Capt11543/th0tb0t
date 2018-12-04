import asyncio
import discord

client = discord.Client()

token = "that's a no from me chief"
prefix = '-'

jump_lyrics = [ "I get up, and nothin' gets me down",
                "You got it tough, I've seen the toughest around",
                "And I know, baby, just how you feel",
                "You got to roll with the punches and get to what's real",
                "Ah, can't you see me standin' here",
                "I got my back against the record machine",
                "I ain't the worst that you've seen",
                "Ah, can't you see what I mean?",
                "Ah, might as well jump",
                "Might as well jump",
                "Go ahead an' jump",
                "Go ahead and jump",
                "Ow oh, hey you",
                "Who said that?",
                "Baby, how you been?",
                "You say you don't know",
                "You won't know until you begin",
                "Ah, can't you see me standin' here" ]

@client.event
async def on_ready():
  print("th0t b0t has arrived")

@client.event
async def on_message(message):
  if message.author != client.user:
    for idx, str in enumerate(jump_lyrics):
      if message.content.lower() == str.lower():
        await client.send_message(message.channel, jump_lyrics[idx + 1])
        print("Jump lyrics time")

    # help command          
    if message.content.startswith(prefix + "help"):
      help_embed = discord.Embed(color = discord.Colour.red())  # Set up embed
      help_embed.set_author(name = "Help")  # Embed title (because the actual title field isn't very useful)
      help_embed.add_field(name = "-help", value = "Shows this message", inline = False)  # Add field that describes the help command
      help_embed.add_field(name = "-ping", value = "Pong!", inline = False)  # Add field that describes the ping command
      help_embed.add_field(name = "-say", value = "th0t b0t will say anything you want it to!  He'll even delete your request, to hide the evidence.  (Please be nice!)")  # Add field that describes the say command

      await client.send_message(message.channel, embed=help_embed) # Temporary help message, replace with command names and possibly add a link to dueling rules doc
      print("halppls") # Tells me that someone is asking for help with the bot, and that you should answer their questions
    
    if message.content.startswith(prefix + "ping"):
      await client.send_message(message.channel, "Pong!")
      print("Pong!")
    
    # say command
    if message.content.startswith(prefix + "say"):
      if len(message.content) > 5:  # Checks that the user actually included something for the bot to say
        output = message.content[5:]  # Stores the desired output into its own variable

        await client.send_message(message.channel, output)  # Responds with the desired message
        await client.delete_message(message)  # Deletes the original message (to hide the evidence!)

        print("OK, there, I said it!")  # Lets me know that someone has triggered this action successfully
      else:
        await client.send_message(message.channel, "Come on, man, you gotta give me something to say!")  # Lets user know that they didn't provide enough information

        print("I didn't say anything.  I couldn't say anything!")  # Lets me know that someone has triggered this action unsuccessfully

  if message.channel.id == "515574829592608769" and message.content.lower() != "f":
    await client.delete_message(message)
    print("PRESS F ONLY :reee:")
  
  # Quarantining OwOs
  if not message.channel.id == "515575113945710593" and "owo" in message.content.lower() or "uwu" in message.content.lower():  # Checks for messages containing "owo" or "uwu"
    await client.delete_message(message)  # Deletes messages
    await client.send_message(message.channel, "git ur stinkin anime outta my channel, t h 0 t")  # Responds with a meme-y message
    
    print("OwO quarantined successfully")  # Tells me that someone OwOd

client.run(token)
