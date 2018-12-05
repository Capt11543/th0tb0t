'''
th0t b0t by Capt#4328
Note to collaborators: The indentation for this program is 2 spaces!
'''

# Import modules
import asyncio
import discord
from dueling import Duel

client = discord.Client()  # Create a client for the bot to use to do things

token = "that's a no from me chief"
prefix = '-'  # Prefix for commands

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
                "Ah, can't you see me standin' here" ]  # Stores all the lines of Jump by Van Halen

@client.event
async def on_ready():
  print("th0t b0t has arrived")  # Lets me know that the bot is working

@client.event
async def on_message(message):  # Will run whenever message is sent
  if message.author != client.user:  # Makes sure that the bot can't trigger itself
    for idx, string in enumerate(jump_lyrics):  # Checks for the message containing any of the lines of Jump
      if message.content.lower() == string.lower():
        await client.send_message(message.channel, jump_lyrics[idx + 1])  # Responds with the next line in the sequence
        print("Jump lyrics time")  # Lets me know that someone has triggered this action
        
    # ping command
    if message.content.startswith(prefix + "ping"):
      await client.send_message(message.channel, "Pong!")  # Sends reply
      print("Pong!")  # Lets me know that someone has triggered this action
        
    # Duel related commands!
    if message.content.startswith(prefix + "sahdude") and active_duel == 0:  # sahdude command if there is not an active duel
      # Checks that there is exactly 1 mention in the message
      if len(message.mentions) == 1:
        target = message.mentions[0]  # Stores the mention in the message in a variable

        # Alert opponent about duel challenge
        await client.send_message(message.channel, "Heads up " + target.mention + "!  " + message.author.mention + " has challenged you to a duel!")
        await client.send_message(message.channel, "To accept the duel, type -sahdude back.  To decline, type -fingerguns.")
        active_duel = Duel(message, client, message.author, target)

        print("Someone challenged someone else to a duel!")
    elif len(message.mentions) < 1:  # In case they didn't mention anyone
      await client.send_message(message.channel, "You must mention your desired opponent!")
    elif len(message.mentions) > 1:  # In case they mention more than one person
      await client.send_message(message.channel, "Easy there!  You can only duel one person at a time!")
    elif message.content.startswith(prefix + "sahdude") and not active_duel == 0 and message.author == active_duel.player2:  # sahdude command if there is an active duel and the user is the challenged
       # Notify the user that the duel was accepted successfully
      await client.send_message(message.channel, "Hey, look at that!  You accepted the duel!")
      await client.send_message(message.channel, "Soon, more stuff is going to happen, but in the meantime, just enjoy this moment!")
    elif message.content.startswith(prefix + "sahdude") and not active_duel == 0 and not message.author == active_duel.player2:
      await client.send_message(message.channel, "There's already a duel going on and you weren't challenged to it.  Sorry!")  # Notify the user that they can't use this command at the moment
    if message.content.startswith(prefix + "fingerguns") and active_duel == 0 or (not active_duel == 0 and not message.author == active_duel.player2):  # fingerguns command for when the user is not challenged or there is no duel (it will have the same output either way)
       await client.send_message(message.channel, "You are not being challenged to a duel!")  # Notify the user that they are not challenged to a duel
    elif message.content.startswith(prefix + "fingerguns") and not active_duel == 0 and message.author == active_duel.player2:
        await client.send_message(message.channel, active_duel.player1 + " It looks like your opponent has surrendered.  Oh well, maybe next time!")  # Notifies challenger of surrender

        active_duel = None  # Resets active_duel to None

  if message.channel.id == "512980566501490700" and message.content.lower() != "f":  # Checks for messages that aren't "f" in #press-f (not case-sensitive)
    await client.delete_message(message)  # Deletes the offending message
    print("PRESS F ONLY :reee:")  # Lets me know that someone has triggered this action

client.run(token)
