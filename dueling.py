# Imports
import async
import discord
import main

class Player:  # Class used to represent each player in a duel
    def __init__(discord_id):  # Constructor
      this.discord_id = discord_id  # Stores the Discord ID of the player involved

      if not Path(discord_id + ".txt").is_file():  # Checks to see if there's a save file for this person
        self.save_file = open(discord_id + ".txt",'w')  # If not, create one
      else:
        self.save_file = open(discord_id + ".txt",'r')  # If there is, read from it

class Duel: # Class for doing duels
  def __init__(self, message, player1, player2):  # Constructor
    self.message = message  # Allows me to pass in the message variable from on_message, so there's no errors
  
    # Objects of the Player class that represent the players
    self.player1 = Player(player1)
    self.player2 = Player(player2)
