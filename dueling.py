# Imports
import asyncio
import discord

class Player:  # Class used to represent each player in a duel
    def __init__(self, member):  # Constructor
        self.member = member  # Stores the Discord ID of the player involved

        self.choice = None  # Creates an empty variable to store their choice in

        print("Player object created successfully with ID " + self.member.id)  # Lets me know that the Player object worked

    def get_accept(self, prefix, content):  # Determines whether player2 accepts or rejects the duel
        if content.startswith(prefix + "sahdude"):  # Accepted
            return True
            self.phase += 1  # Move the duel on to the next phase
        if content.startswith(prefix + "fingerguns"):  # Rejected
            return False

class Duel: # Class for doing duels
    def __init__(self, player1, player2):  # Constructor
        # Objects of the Player class that represent the players
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.phase = 0  # What phase the duel is on.  0 = challenge, 1 = choosing, 2 = throwing, 3 = results

        print("Duel object created successfully")  # Lets me know that the Duel object worked
