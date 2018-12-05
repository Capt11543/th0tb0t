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
        
    try:  # Everything duel-related!
      if active_duel.phase == 0:  # Challenge phase (does player 2 accept?)
        if message.author == active_duel.player2.member:
          if active_duel.player2.get_accept(prefix, message.content):  # Accepted
            await client.send_message(message.channel, active_duel.player1.member.mention + " The duel has been accepted!  May the fight begin!")  # Alerts player 1 that the duel was accepted
                    
            print ("Duel accepted!  The duel is on phase " + active_duel.phase + ".")  # Lets me know that everything worked properly
          else:  # Denied
            await client.send_message(message.channel, active_duel.player1.member.mention + " The duel was surrendered.  Better luck next time!")  # Alerts player 1 that the duel was denied
            del active_duel  # Removes the duel object from
            
            print("Duel denied.")
    except NameError:  # If active_duel doesn't exist
      if message.content.startswith(prefix + "sahdude"):  # sahdude command to initiate a duel
        # Checks that there is exactly 1 mention in the message
        if len(message.mentions) == 1:
          active_duel = Duel(message.author, message.mentions[0])

          # Alert opponent about duel challenge
          await client.send_message(message.channel, "Heads up " + active_duel.player2.member.mention + "!  " + active_duel.player1.member.mention + " has challenged you to a duel!")
          await client.send_message(message.channel,  "To accept the duel, type -sahdude back.  To decline, type -fingerguns.")
          
          print("Someone challenged someone else to a duel!")
        elif len(message.mentions) < 1:  # In case they didn't mention anyone
          await client.send_message(message.channel, "You must mention your desired opponent!")
        elif len(message.mentions) > 1:  # In case they mention more than one person
          await client.send_message(message.channel, "Easy there!  You can only duel one person at a time!")
      else:  # If they're trying to use another duel-related command
        await client.send_message(message.channel, "There is no duel going on right now!")  # Lets the user know that their input was invalid 

  if message.channel.id == "512980566501490700" and message.content.lower() != "f":  # Checks for messages that aren't "f" in #press-f (not case-sensitive)
    await client.delete_message(message)  # Deletes the offending message
    print("PRESS F ONLY :reee:")  # Lets me know that someone has triggered this action

client.run(token)
