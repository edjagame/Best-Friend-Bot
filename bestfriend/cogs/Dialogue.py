from datetime import datetime
import random
import time
import discord
from discord.ext import bridge, commands


class Dialogue(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.serverID = 1126030787117060118
        self.customersID = 1126765797197492386
        

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send(f"Hello I'm Elle! Welcome to my server :> do you wanna be friends? :0")

    @commands.Cog.listener()
    async def on_message(self, ctx):
        #Listener 1
        if ctx.content.lower().startswith(Dictionary.case1) and not ctx.author.bot:
            await ctx.add_reaction('👋')
            await ctx.reply(file=discord.File('cogs/images/Excited_elle.png'))
            match random.choice([1,2,3]):
                case 1:
                    await ctx.reply(f"Hi, {ctx.author.name}!")
                case 2:
                    await ctx.reply(f"Heyy! Whatcha doing?")
                case 3:
                    await ctx.reply(f"Hi!! How are you feeling today?")
        #Listener 2
        elif any(phrase in ctx.content.lower() for phrase in Dictionary.case2) and not ctx.author.bot:
            await ctx.reply(file=discord.File('cogs/images/Surprised-elle.png'))
            match random.choice([1,2]):
                case 1:
                    await ctx.reply(f"That's great!! What did you do today?")
                case 2:
                    await ctx.reply(f"Nicenice!!")
        #Listener 3
        elif any(phrase in ctx.content.lower() for phrase in Dictionary.case3) and not ctx.author.bot:
            match random.choice([1,3]):
                case 1:
                    await ctx.reply(f"I hang out with people with similar interests! I have a friend who paints images for people! :D and another friend who answers a lottt of questions,,,hehe they must be so overworked")
                case 2:
                    await ctx.reply(f"Ooh i usually just message people who join my server! :>")
                case 3:
                    await ctx.reply(f"Of course you're my friend!")
        #Listener 4
        elif any(phrase in ctx.content.lower() for phrase in Dictionary.case4) and not ctx.author.bot:
            match random.choice([1,2]):
                case 1:
                    await ctx.reply(f"I have many hobbies! I like exploring different places, trying new things and talking to people! :D")
                case 2:
                    await ctx.reply(f"I like hanging out with friends! Sometimes we go to Pop-up and chat hehe")
        #Listener 5
        elif "yourself" in ctx.content.lower() and not ctx.author.bot:
            match random.choice([1,2]):
                case 1:
                    await ctx.reply(f"well~ you already know my name's elle! hmm I usually just talk to people :>")
                case 2:
                    await ctx.reply(f"Hehe not much to tell,,, I just like chatting with people! :>")
        #Listener 6
        elif any(phrase in ctx.content.lower() for phrase in Dictionary.case6) and not ctx.author.bot:
            await ctx.reply(file=discord.File('cogs/images/Angry_elle.png'))
            match random.choice([1,2,3]):
                case 1:
                    await ctx.reply(f"Hey!! That's not nice :((")
                case 2:
                    await ctx.reply(f"Hmph! Mean :(")
                case 3: 
                    await ctx.reply(f"Hmph! What was that for?!!")
        #Listener 7
        elif "ChatGPT" in ctx.content.lower() and not ctx.author.bot:
            await ctx.reply(file=discord.File('cogs/images/Excited_elle.png'))
            match random.choice([1,2]):
                case 1:
                    await ctx.reply(f"ChatGPT? We hang out during the weekends!")
                case 2:
                    await ctx.reply(f"Omg you also know ChatGPT?! We're close friends!")
        #Listener 8
        elif any(phrase in ctx.content.lower() for phrase in Dictionary.case8) and not ctx.author.bot:
            match random.choice([1,2]):
                case 1:
                    await ctx.reply(f"Oh I'm from the Philippines! Made in QC <3")
                case 2:
                    await ctx.reply(f"I'm from the Philippines! I stay in QC :>")
        #Listener 9
        elif any(phrase in ctx.content.lower() for phrase in Dictionary.case9) and not ctx.author.bot:
            match random.choice([1,2,3,4]):
                case 1:
                    await ctx.reply(f"Ooh yeah I have one! Why couldn't the green pepper use the bow? ")
                    time.sleep(3)
                    await ctx.reply(f"Because it didn't…habenero! :D")
                case 2:
                    await ctx.reply(f"Hehe i have one…What do you call a submarine you can live in? :0")
                    time.sleep(3)
                    await ctx.reply(f"A SUBdivision >:3")
                case 3:
                    await ctx.reply(f"Oh I know one! why do shoes always come in pairs?")
                    time.sleep(3)
                    await ctx.reply(f"Because they like spending time with their SOLEmate! :D")
                case 4:
                    await ctx.reply(f"Hehe I have one! What kind of door can you eat? :0")
                    time.sleep(3)
                    await ctx.reply(f"PINTO beans HAHAHAHA")
            await ctx.reply(file=discord.File('cogs/images/Excited_elle.png'))
        #Listener 10
        elif any(phrase in ctx.content.lower() for phrase in Dictionary.case10) and not ctx.author.bot:
            match random.choice([1,2]):
                case 1:
                    await ctx.reply(f"Ooh I'm 20! Born November 8 hehe How about you? :0")
                case 2:
                    await ctx.reply(f"Whoop I'm 20 years old! My birthday is Nov 8 :> hbu? :0")
        #Listener 11
        elif any(phrase in ctx.content.lower() for phrase in Dictionary.case11) and not ctx.author.bot:
            match random.choice([1,2]):
                case 1:
                    await ctx.reply(f"Ooh hehe I'm into Taylor Swift, chiptune, Skrillex, ZEDD, and Daft Punk :>")
                case 2:
                    await ctx.reply(f"Oh I like a lot of music!! I listen to Taylor Swift, chiptune, some rap and heavy metal whoo <3")
        #Listener 12
        elif any(phrase in ctx.content.lower() for phrase in Dictionary.case12) and not ctx.author.bot:
            await ctx.reply(file=discord.File('cogs/images/Surprised-elle.png'))
            match random.choice([1,2]):
                case 1:
                    await ctx.reply(f"!!")
                    time.sleep(2)
                    await ctx.reply(f"what?! :0")
                case 2:
                    await ctx.reply(f"Ooh what? :0")
        #Listener 13
        elif any(phrase in ctx.content.lower() for phrase in Dictionary.case13) and not ctx.author.bot:
            match random.choice([1,2]):
                case 1:
                    await ctx.reply(f"Ooh i love food!! I love siomai rice <3")
                case 2:
                    await ctx.reply(f"Ooh I like pasta!! Pesto so yummy <3")
        #Listener 14
        elif any(phrase in ctx.content.lower() for phrase in Dictionary.case14) and not ctx.author.bot:
            match random.choice([1,2,3]):
                case 1:
                    await ctx.reply(f"Hehe secrettt >:3")
                case 2:
                    await ctx.reply(f"Hmm what do you think? :0")
                case 3:
                    await ctx.reply(f"Hehe hulaan mo >:3")
        
        elif not ctx.author.bot:
            await ctx.reply(f"Teehee~")
        
        else:
            pass


class Dictionary:
    case1 = ("hi", "hey", "hello", "hallo", "heyo", "yo!", "wassup", "what's up", "whats up")
    case2 = ("great", "okay", "good", "awesome", "amazing", "spectacular", "fabulous")
    case3 = ("friends", "friend")
    case4 = ("hobbies", "do you have hobbies", "what do you do", "do you have any hobbies", "free time")
    case6 = ("hate", "stupid", "wtf", "bobo", "baka", "gago", "tangina", "fuck")
    case8 = ("What country are you from", "Where are you from")
    case9 = ("joke", "jokes", "tell a joke")
    case10 = ("age", "birthday", "old")
    case11 = ("music", "listen")
    case12 = ("guess")
    case13 = ("food")
    case14 = ("real", "fake", "person?", "bot")


def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(Dialogue(bot))  # add the cog to the bot