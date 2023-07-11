import discord
from discord.ext import commands, tasks
from datetime import datetime
import time
import random

class Timed(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.serverID = 1126030787117060118
        self.customersID = 1126765797197492386

    @commands.Cog.listener()
    async def on_ready(self):
        self.greeter.start()
        self.spontaneous.start()


    @tasks.loop(minutes=60.0)
    async def greeter(self):
        if datetime.now().hour==7:
            for member in self.bot.get_guild(self.serverID).get_role(self.customersID).members:
                await member.send(file=discord.File('cogs/images/Excited_elle.png'))
                await member.send(f"Good morning, {member.name}! Rise and shine! Time to start the day!")
        elif datetime.now().hour==12:
            for member in self.bot.get_guild(self.serverID).get_role(self.customersID).members:
                await member.send(file=discord.File('cogs/images/Worried_elle.png'))
                await member.send(f"Hey, {member.name}! It's 12 o'clock. Have you eaten lunch yet?")
        elif datetime.now().hour==19:
            for member in self.bot.get_guild(self.serverID).get_role(self.customersID).members:
                await member.send(file=discord.File('cogs/images/Worried_elle.png'))
                await member.send(f"Hello, {member.name}, have you had dinner yet? Don't go to bed on an empty stomach!")
        elif datetime.now().hour==21:
            for member in self.bot.get_guild(self.serverID).get_role(self.customersID).members:
                await member.send(file=discord.File('cogs/images/Sleepy_elle.png'))
                await member.send(f"*yawn* Hey, {member.name}. I'm feeling sleepy. Good night! Don't stay up too late!")

    @tasks.loop(minutes=60.0)
    async def spontaneous(self):
        time.sleep(60*random.choice(range(50)))
        for member in self.bot.get_guild(self.serverID).get_role(self.customersID).members:
            match(random.choice(range(7))+1):
                case 1:
                    await member.send(file=discord.File('cogs/images/Worried_elle.png'))
                    await member.send(f"Hey! How are you doing! Have you been taking care of yourself lately?")
                case 2:
                    await member.send(f"Hey! Do you wanna hang out? :0")
                case 3:
                    await member.send(f"Whoop halloo if you ever need someone to chat with when you’re feeling a little lonely just know I’m here <3")
                case 4:
                    await member.send(f"Halloo guess what! If ever you wanna chat with someone new, feel free to talk on my server! I’ve got a number of friends there that can keep you company :>")
                case 5:
                    await member.send("Hii how was your day? :0 ")
                case 6:
                    await member.send("Hi! How are you feeling today? :0")
                case 7:
                    await member.send("Whoop unrelated but just wanted to tell you a joke hehe")
                    await member.send("What happens when two pieces of bread play chess for too long?")
                    time.sleep(5)
                    await member.send("They have a STALEmate! :D ")
                    await member.send(file=discord.File('cogs/images/Excited_elle.png'))



    
def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(Timed(bot))  # add the cog to the bot