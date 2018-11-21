import asyncio
import discord

client = discord.Client()

token = "NTE0NTg4NDc2MDIxMTQ1NjAx.DtYvyQ.W-nuoz4GQQJbHdqrWL09zYmtegw"

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

    if message.channel.id == "512980566501490700" and message.content.lower() != "f":
        await client.delete_message(message)
        print("PRESS F ONLY :reee:")

client.run(token)