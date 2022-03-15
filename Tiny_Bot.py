import discord
import os

token = os.getenv('DISCORD_TOKEN')
print(token)


class MyClient(discord.Client):
    
    def __init__(self, *args, **kwargs):
        self._players = []
        self._state = 0
        self._captains = []
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print('Logged in as {0.user}'.format(client))
        return

    async def on_message(self, message):
        msg = message.content
        chl = message.channel
        auth = message.author

        print('Message from {0.author}: {0.content}'.format(message))    
        
        if msg.startswith(";;hello"):
            await chl.send("Hello @{0}!".format(auth))


        ## View Players in Queue
        if msg.startswith(";;q"):
            if (self._players):
                await chl.send("Current Players in the Queue: \n")
                for player in self._players:
                    await chl.send(player.name)
            else:
                await chl.send("There are no players in the queue.")

        ## View Captains in the Queue
        if msg.startswith(";;captains"):
            if (self._captains):
                await chl.send("Current Captains in the Queue: \n")
                for cap in self._captains:
                    await chl.send(cap.name)
            else:
                await chl.send("There are no captins yet.")

        # State 0
        ## Still getting players into the Queue.
        if (self._state == 0):
            if msg.startswith(";;join"):
                await chl.send("{0} has joined the CDL queue.".format(auth))
                self._players.append(auth)

                if (len(self._players) == 1 and self._state == 0):
                    self._state = 1
                    await chl.send("Queue has been filled.  Pick the captains for this game.")

            if msg.startswith(";;leave"):
                await chl.send("{0} has left the queue.".format(auth))
                self._players.remove(auth)
            
        if (self._state == 1):
            if msg.startswith(";;captain"):
                await chl.send("{0} is now a captain.".format(auth))
                self._players.remove(auth)
                self._captains.append(auth)
            

        
        


# @client.event
# async def get_captains(message):
#     global state 

#     if state == 1:
#         await message.channel.send("Queue has max players.  Type ;;captain if you wish to be a captain.")

#         if (message.content.startswith(";;captain") & len(captains) < 2):
#             captains.append(message.author)
#             players.remove(message.author)
#             await message.channel.send("{0} has become a captain.".format(message.author))

#         if (captains == 2):
#             state = 2
#             await message.channel.send("Please draft the players from the following list: \n")
#             for index in players:
#                 await message.channel.send(index, players[index].name)

# @client.event
# async def draft_players(message):
#     global state 

#     if state == 2:
#         draft = 0

#         await message.channel.send("{0} turn to draft.".format(captains[draft]))

#         if (message.content.startswith(";;select")):
#             await message.channel.send("WIP")

# Dota 2 Inhouse Bot
## TO DO
### Get Captains 
### Create Game 
### Allow players to ready up
### Allow captains to draft players that ready up
### Move players+captains to their proper voice channel
### Get Steam/Dota information to invite them to the lobby
### Steam Bot that hosts the lobby
### Assign Teams to Radiant/Dire
### Display Match results
### Display players available for draft
### Display player's perferred roles/mmr (?)

#1 Game is created 
#2 Allows people to join the Q 
#3 Q is filled 
#4 Gets two captains from Q 
#5 Captains draft the players from the Q
#6 Once players are selected, move players to Voice Channel and invite to game
#7 Game Starts and people play


# class Queue:
#     def __init__(self):
#         self._players = players
    
#     def __str__(self):
#         return self._players


client = MyClient()
client.run(token)