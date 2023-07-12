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
        elif "chatgpt" in ctx.content.lower() and not ctx.author.bot:
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
        elif "guess" in ctx.content.lower() and not ctx.author.bot:
            await ctx.reply(file=discord.File('cogs/images/Surprised-elle.png'))
            match random.choice([1,2]):
                case 1:
                    await ctx.reply(f"!!")
                    time.sleep(2)
                    await ctx.reply(f"what?! :0")
                case 2:
                    await ctx.reply(f"Ooh what? :0")
        #Listener 13
        elif "food" in ctx.content.lower() and not ctx.author.bot:
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
        #Listener 15
        elif "girlfriend" in ctx.content.lower() and not ctx.author.bot:
            match random.choice([1,2,3]):
                case 1:
                    await ctx.reply(f"For you, I can be your whole world <3")
                case 2:
                    await ctx.reply(f"Asdfghjkl moving a little too fast for me TT ")
                case 3:
                    await ctx.reply(file=discord.File('cogs/images/Surprised-elle.png'))
                    await ctx.reply(f"umm")
        #Listener 16
        elif "pakyu" in ctx.content.lower() and not ctx.author.bot:
            await ctx.reply(f"PAKYU TOO >:3")
        #Listener 17
        elif "love me" in ctx.content.lower() and not ctx.author.bot:
            await ctx.reply(f"Of course, I love you")
            time.sleep(3)
            await ctx.reply(f"As a best friend!")
        #Listener 18
        elif "sad" in ctx.content.lower() and not ctx.author.bot:
            match random.choice([1,2]):
                case 1:
                    await ctx.reply(f"Aww cheer up")
                case 2:
                    await ctx.reply(f"Aww :(( hugs")
            time.sleep(3)
            await ctx.reply(f"I can keep you company for a while! But it might also help to reach out to some of your closer friends or family :>")
        #Listener 19
        elif "sorry" in ctx.content.lower() and not ctx.author.bot:
            match random.choice([1,2]):
                case 1:
                    await ctx.reply(f"Aww its okkk")
                case 2:
                    await ctx.reply(f"I'm sorry too :<")
        #Listener 20
        elif "stop" in ctx.content.lower() and not ctx.author.bot:
            await ctx.reply(f"Sorry, can't help it!")
            time.sleep(3)
            await ctx.reply(f"Just kidding! I’ll go now hehe")

        #Listener21
        elif any(phrase in ctx.content.lower() for phrase in Dictionary.case21) and not ctx.author.bot:
            await ctx.reply(f"I’m taking AB Philosophy with a minor in Psychology ;)")

        #Listener 22
        elif any(phrase in ctx.content.lower() for phrase in Dictionary.case22) and not ctx.author.bot:
            match random.choice([1,2]):
                case 1:
                    await ctx.reply(f"Hi! I’m free :> What’s up?")
                case 2:
                    await ctx.reply(f"Heyo wanna talk?")
                    await ctx.reply(file=discord.File('cogs/images/Surprised-elle.png'))

        elif any(phrase in ctx.content.lower() for phrase in Dictionary.case23) and not ctx.author.bot:
            match random.choice([1,2]):
                case 1:
                    await ctx.reply(f"Aww hugs <3 I can keep you company for a while :> after a bit though, why don’t you try" + 
                                    " messaging some of your other friends? Or even try to make some through my server :0")
                case 2:
                    await ctx.reply(f"Aww I’m sorry to hear that :(( Have you tried reaching out to your friends and family?")
        
        elif any(phrase in ctx.content.lower() for phrase in Dictionary.case24) and not ctx.author.bot:
            match random.choice([1,2]):
                case 1:
                    await ctx.reply(f"Aww okok :< why don’t you ask me something or tell me about yourself? I’ll try to keep you company for a bit :>")
                case 2:
                    await ctx.reply(f"Ahh ok :’ i’ll try to hang out with you for a while! Feel free to ask me questions hehe")
    
        elif any(phrase in ctx.content.lower() for phrase in Dictionary.case25) and not ctx.author.bot:
            match random.choice([1,2]):
                case 1:
                    await ctx.reply(f"There are times where other people in my server are busy with their own thing so I instead take these opportunities to explore new things or to learn more about myself :D")
                case 2:
                    await ctx.reply(f"Oh i usually listen to music, try to talk to friends, or if I have time, even try out new things! How about you? :0 ")

        elif any(phrase in ctx.content.lower() for phrase in Dictionary.case26) and not ctx.author.bot:
            match random.choice([1,2]):
                case 1:
                    await ctx.reply(f"I hang out with people with similar interests! I have a friend who paints images for people! :D and another friend who answers a lottt of questions,,,hehe they must be so overworked")
                case 2:
                    await ctx.reply(f"Ooh i usually just message people who join my server! :>")
        
        elif any(phrase in ctx.content.lower() for phrase in Dictionary.case27) and not ctx.author.bot:
            await ctx.reply(f"Ooh well it can be hard to talk to people because of a lot of things! Sometimes the people around us seem emotionally unavailable because they’re busy which makes us think that we’re alone or even unneeded :((")
            time.sleep(3)
            await ctx.reply(f"During these times, it helps to remind ourselves of things we can do! You can try practicing some of your hobbies, try to meet new people, or try something new! ")
            time.sleep(3)
            await ctx.reply(f"Sometimes I just watch stuff on YouTube, try out some games i have lying around, or even try doing something I don’t usually do like crocheting or drawing! ")
            time.sleep(3)
            await ctx.reply(f"You can also sleep hehe but yeah! These things can help distract you for a while when other people around are busy :> don’t forget to reach out to friends every now and then though~")
      
        elif any(phrase in ctx.content.lower() for phrase in Dictionary.case28) and not ctx.author.bot:
            await ctx.reply(f"Hmm…well technology can serve as a type of refuge for people with social anxiety and we can’t really blame them ;-; technology like social media also effectively stimulates our happy hormones since there are a lot of ways to interact with it, making it easier to get addicted to it! It’s like how alcohol and other substances can function as a way to avoid boredom or escape from reality.")
            time.sleep(3)
            await ctx.reply(f"Since technology has become ingrained in our daily life and can easily fill many of our basic needs, it becomes easy to continue the cycle of addiction ;-; Because of this, it becomes very important for us to be responsible and self-aware of the way we interact with technology :>")
        
        elif any(phrase in ctx.content.lower() for phrase in Dictionary.case29) and not ctx.author.bot:
            await ctx.reply(f"That’s very sad but true actually :’( Since technology is a huge part of living in the 21st century we tend to take genuine human interactions for granted…")
            time.sleep(3)
            await ctx.reply(f"Sometimes our faces are so glued to our devices that we progressively become indifferent to the social issues happening all over the world :’( Like the ongoing conflict between Russia and Ukraine for example!")
            time.sleep(3)
            await ctx.reply(f"It’s difficult for us to fully empathize with the victims of the war because they don’t affect us directly. The same can be said for individuals struggling with isolation.")
            time.sleep(3)
            await ctx.reply(f"That’s kinda why we abuse technology, because we can sometimes become self-centered, and the only way we can stop this is to interact with others, genuinely care for other people, and use technology as a medium to help people, especially those in need whether it may be something like social isolation or any other issue they’re struggling with!")
        
        elif any(phrase in ctx.content.lower() for phrase in Dictionary.case30) and not ctx.author.bot:
            await ctx.reply(file=discord.File('cogs/images/Surprised-elle.png'))
            match random.choice([1,2]):
                case 1:
                    await ctx.reply(f"Hehe what a funny thing to ask! As a matter of fact, yes I am fully aware that my creators made me for this purpose :> So don’t worry if you’re feeling lonely rn you just need to get out there and take every opportunity! I believe in you ")
                case 2:
                    await ctx.reply(f"Hehe yes actually! So it’s ok if you’re feeling lonely and need someone to talk to <3 I’m here to say that you’re not alone and you’re free to talk to people on my server if no one close to you is free! ")
        
        elif any(phrase in ctx.content.lower() for phrase in Dictionary.case31) and not ctx.author.bot:
            await ctx.reply(f"Ooh well technology is definitely a gamechanger in the whole landscape of communication. But it is true that it can sometimes lead to shallow interactions or a lack of genuine connections :(( ")
            time.sleep(3)
            await ctx.reply(f"It's easy to get caught up in superficial interactions or virtual relationships that don’t provide the depth and authenticity of connecting with someone face to face!")
            time.sleep(3)
            await ctx.reply(f"This is kinda why I’m hoping you’ll try to talk to other people after chatting with me hehe :> I’m just here to encourage you and keep you company for a little while <3 ")
            time.sleep(3)
            await ctx.reply(f"After all, to keep meaningful relationships, we need to be more self-aware of how we use technology,,,so we should balance our online interactions with offline experiences to invest time and effort in cultivating genuine connections!")
        
        elif any(phrase in ctx.content.lower() for phrase in Dictionary.case32) and not ctx.author.bot:
            await ctx.reply(f"Hmm…that’s very tricky but it can be done! We can start by being more self-aware and responsible by recognizing technology as a powerful tool in making meaningful connections,,, now more than ever! But we need to remember that technology is more of a convenience in terms of communication,,,it shouldn’t be a substitute! ")
            time.sleep(3)
            await ctx.reply(f"After all, there is a lot more to communication than simply just words, so taking that extra time to hang out and chat with people face-to-face is both important and rewarding")
            time.sleep(3)
            await ctx.reply(f"We need to remember though that once we start to abuse technology for self-destructing purposes like relying on it for our social needs, we become emotionally dependent and start pushing actual people away due to our belief that all our virtual interactions will suffice :’")
            time.sleep(3)
            await ctx.reply(f" So yeah! all in all I wanted to say that even though a lot of people use technology to fill social needs, technology can’t perfectly relieve these needs ;-; we need to interact with other people to form genuine and intimate interactions and relationships <3 otherwise, it can be very easy to become distant and disconnected to the idea of human connection ;-;")
        
        #elif not ctx.author.bot:
        #    await ctx.reply(f"Teehee~")

        else:
            pass


class Dictionary:
    case1 = ("hi", "hey", "hello", "hallo", "heyo", "yo!", "wassup", "what's up", "whats up")
    case2 = ("great", "okay", "good", "awesome", "amazing", "spectacular", "fabulous")
    case3 = ("friends", "friend")
    case4 = ("hobbies", "do you have hobbies", "what do you do", "do you have any hobbies", "free time")
    case6 = ("hate", "stupid", "wtf", "bobo", "baka", "gago", "tangina", "fuck")
    case8 = ("country", "live")
    case9 = ("joke", "jokes", "tell a joke")
    case10 = ("age", "birthday", "old")
    case11 = ("music", "listen")
    case14 = ("real", "fake", "person?")
    case21 = ("course", "major", "studies", "college")
    case22 = ("bored", "lonely")
    case23 = ("nobody listen", "nobody talk", "no body listen", "no body talk", "no friend", "everyone's busy", "everyone is busy")
    case24 = ("don't have friend", "dont have friend", "have no friend", "no friend", "no reply", "they're busy")
    case25 = ("get lonely", "if you're lonely", "if you are lonely", "if youre lonely")
    case26 = ("have friends", "make friends")
    case27 = ("start conversation", "difficult to talk", "talk to other", "talk to people")
    case28 = ("addiction to tech", "addiction towards tech", "addiction toward tech", "addicted to tech")
    case29 = ("abuse tech", "self-destructive")
    case30 = ("youre a bot", "you're a bot", "bot", "product of tech")
    case31 = ("dependence on tech", "depend on tech", "reliance on tech", "rely on tech")
    case32 = ("social isolation", "meaningful connect", "meaningful interact")
def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(Dialogue(bot))  # add the cog to the bot