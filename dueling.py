# Imports
import asyncio
import discord

class Player:  # Class used to represent each player in a duel
  def __init__(self, client, member):  # Constructor
    self.member = member  # Stores the Discord ID of the player involved

    self.choice = None  # Creates an empty variable to store their choice in

    print("Player object created successfully with ID " + self.member.id)  # Lets me know that the Player object worked

class Duel: # Class for doing duels
  def __init__(self, message, client, player1, player2):  # Constructor
    self.message = message  # Allows me to pass in the message variable from on_message, so there's no errors
    # Objects of the Player class that represent the players
    self.player1 = Player(client, player1)
    self.player2 = Player(client, player2)
    self.phase = 1  # What phase the duel is on.  1 = choosing, 2 = throwing, 3 = results

    print("Duel object created successfully")  # Lets me know that the Duel object worked
