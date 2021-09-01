from random import randrange, choice, randint
import discord
import asyncio
import time
from requests import get
from datetime import datetime

TOKEN_AUTH = "MzA0NjU1NzI0ODQ2MzgzMTA0.YS-nIA.f_6OxvEwvJsL9_A095CczakVI7M" # YOUR TOKEN HERE
ip = "" # YOUR IP HERE, LEAVE BLANK IF YOU DONT USE A VPN
username = "madetheheadline" # YOUR USERNAME HERE, THE THING PEOPLE CALL U
now = datetime.now()

current_time = now.strftime("%H:%M:%S")


client = discord.Client()
@client.event
async def on_ready():
    print(client.guilds)
    
ban = []
ty = ["appreciate it","tyvm","thanks","Thank you","thank you","thx","tysm"]

class c:
    cache = ""
    sent = []
    can = False
    
@client.event
async def on_reaction_add(reaction, user):
    print(f"Someone reacted! channel: {reaction.message.guild.name} - room id: {reaction.message.channel.id} - room name: {reaction.message.channel.name}")
    if (
        reaction.message.channel.id == 699702250531979325
        or reaction.message.channel.id == 755024910023131167
        or reaction.message.channel.id == 639195586070839316
        or reaction.message.channel.id == 836093933121437728
        or reaction.message.channel.id == 844088510364254208
        or reaction.message.channel.id == 838161684501364766
        or reaction.message.channel.id == 731110557389946915
        or reaction.message.channel.id == 704454414533918807
        or reaction.message.channel.id == 741405810130813009
        or reaction.message.channel.id == 764036400449585172
        or reaction.message.channel.id == 858620206610645002
        or reaction.message.channel.id == 683726957019791419
        or reaction.message.channel.id == 566973676608552972
        or reaction.message.channel.id == 480446343962427410
        or reaction.message.channel.id == 727165393587798016
        or reaction.message.channel.id == 850714241521811489
        or reaction.message.channel.id == 838471968758956103
        or reaction.message.channel.id == 838203397252448336
        or reaction.message.channel.id == 862216679302758440
        or reaction.message.channel.id == 862221767619379200
        or reaction.message.channel.id == 848464764890775565
        or reaction.message.channel.id == 798113216575963156
        or reaction.message.channel.id == 857105467847081994
        or reaction.message.channel.id == 845808399135932416
        or reaction.message.channel.id == 794870696064319489
        or reaction.message.channel.id == 835095534397554730
        or reaction.message.channel.id == 860554847987695666
        or reaction.message.channel.id == 846568929148665856
        or reaction.message.channel.id == 839653943663788053
        or reaction.message.channel.id == 840634427734491149
        or reaction.message.channel.id == 860730663283982367
        or reaction.message.channel.id == 847886919505674280
        or reaction.message.channel.id == 838064306146508851
        or reaction.message.channel.id == 592388493813219378
        or reaction.message.channel.id == 855997796225253407
        or reaction.message.channel.id == 840548870584533072
        or reaction.message.channel.id == 863561401872023582
        or reaction.message.channel.id == 864577424770727947
        or reaction.message.channel.id == 856846853420875789
        or reaction.message.channel.id == 834011712012550146
        or reaction.message.channel.id == 864806761097199616
        or reaction.message.channel.id == 864899529919561758
        or reaction.message.channel.id == 833669087367921674
        or reaction.message.channel.id == 733122024884404287
        or reaction.message.channel.id == 864621111139237889
        or reaction.message.channel.id == 832587922288017408
        or reaction.message.channel.id == 865223569075994678
        or reaction.message.channel.id == 860749184302579743
        or reaction.message.channel.id == 853582688462962778
        or reaction.message.channel.id == 848538017123401728
        or reaction.message.channel.id == 860946228400881704
        or reaction.message.channel.id == 865246261292695553
        or reaction.message.channel.id == 834010498689269761
        or reaction.message.channel.id == 849135991410917396
        or reaction.message.channel.id == 805499485811769374
        or reaction.message.channel.id == 865609261769424897
        or reaction.message.channel.id == 864640738264219658
        or reaction.message.channel.id == 855944490291953664
        or reaction.message.channel.id == 855966103109107753
        or reaction.message.channel.id == 840346883632529428
        or reaction.message.channel.id == 864502624320749658
        or reaction.message.channel.id == 699526998568992839
        or reaction.message.channel.id == 865204415367086080
        or reaction.message.channel.id == 865607084043927600
        or reaction.message.channel.id == 849349912927404122
        or reaction.message.channel.id == 865129082420068352
        or reaction.message.channel.id == 855727330885107712
        or reaction.message.channel.id == 856846801134419979
        or reaction.message.channel.id == 854833733962170378
        or reaction.message.channel.id == 832683597440745472
        or reaction.message.channel.id == 714597353662840834
        or reaction.message.channel.id == 728409594606387210
        or reaction.message.channel.id == 840592521032630302
        or reaction.message.channel.id == 825024614895190098
        or reaction.message.channel.id == 825159579578138704
        or reaction.message.channel.id == 852436512153927731
        or reaction.message.channel.id == 856427377361289226
        or reaction.message.channel.id == 853571695415394312
        or reaction.message.channel.id == 852440014808940575
        or reaction.message.channel.id == 865282805642690560
        or reaction.message.channel.id == 622656117167882241
        or reaction.message.channel.id == 622667519001493515
        or reaction.message.channel.id == 857111174378553354
        or reaction.message.channel.id == 866406077930012673
        or reaction.message.channel.id == 866403509406662657
        or reaction.message.channel.id == 858227988045496351
        or reaction.message.channel.id == 852744345266028545
        or reaction.message.channel.id == 851722952776613918
        or reaction.message.channel.id == 761902290935480330
        or reaction.message.channel.id == 866485799205732372
        or reaction.message.channel.id == 850953525701640203
        or reaction.message.channel.id == 866511748118085642
        or reaction.message.channel.id == 866578608147529768
        or reaction.message.channel.id == 852197046990667796
        or reaction.message.channel.id == 866525858058469377
        or reaction.message.channel.id == 864688193412268042
        or reaction.message.channel.id == 866396935321944114
        or reaction.message.channel.id == 856251959417110589
        or reaction.message.channel.id == 866040327436238898
        or reaction.message.channel.id == 862622334094540840
        or reaction.message.channel.id == 861437335698276394
        or reaction.message.channel.id == 865356741202149387
        or reaction.message.channel.id == 853317842271076382
        or reaction.message.channel.id == 853318242584231936
        or reaction.message.channel.id == 857378657241006089
        or reaction.message.channel.id == 865145316051517451
        or reaction.message.channel.id == 865144504268095489
        or reaction.message.channel.id == 856244633335496735
        or reaction.message.channel.id == 867238599844954122
        or reaction.message.channel.id == 853389431788142612
        or reaction.message.channel.id == 859453483124129794
        or reaction.message.channel.id == 861723948499861544
        or reaction.message.channel.id == 865410590976638996
        or reaction.message.channel.id == 868496467508224000
        or reaction.message.channel.id == 868782741896978452
        or reaction.message.channel.id == 857808471930830859
        or reaction.message.channel.id == 857808852258783293
        or reaction.message.channel.id == 864187144331198475
        or reaction.message.channel.id == 868869530116571136
        or reaction.message.channel.id == 857824893067460649
        or reaction.message.channel.id == 869141403706486815
        or reaction.message.channel.id == 859880666736885820
        or reaction.message.channel.id == 869216232207953960
        or reaction.message.channel.id == 869196725204697180
        or reaction.message.channel.id == 863326251665063956
        or reaction.message.channel.id == 867469106508595231
        or reaction.message.channel.id == 857743446520102953
        or reaction.message.channel.id == 664866493917429800
        or reaction.message.channel.id == 847551251137953793
        or reaction.message.channel.id == 868331142728810546
        or reaction.message.channel.id == 849187351648796702
        or reaction.message.channel.id == 863822831850750013
        or reaction.message.channel.id == 869962769020121169
        or reaction.message.channel.id == 827869693875978240
        or reaction.message.channel.id == 827852905511125022
        or reaction.message.channel.id == 834011457070432297
        or reaction.message.channel.id == 868487069746466897
        or reaction.message.channel.id == 872437352075788359
        or reaction.message.channel.id == 868515837202534401
        or reaction.message.channel.id == 870282200690618458
        or reaction.message.channel.id == 872056725677682728
        or reaction.message.channel.id == 795273749074411540
        or reaction.message.channel.id == 871968898856140810
        or reaction.message.channel.id == 870540233052135446
        or reaction.message.channel.id == 866162345150251008
        or reaction.message.channel.id == 792406224787865640
        or reaction.message.channel.id == 854774008608456714
        or reaction.message.channel.id == 851390051949608985
        or reaction.message.channel.id == 851399024925081652
        or reaction.message.channel.id == 864396482878505012
        or reaction.message.channel.id == 852558812082733076
        or reaction.message.channel.id == 862427707086340136
        or reaction.message.channel.id == 862469840210755584
        or reaction.message.channel.id == 872426137538662400
        or reaction.message.channel.id == 870246745626533928
        or reaction.message.channel.id == 866208648149991454
        or reaction.message.channel.id == 873189472198606910
        or reaction.message.channel.id == 873193888385470545
        or reaction.message.channel.id == 869826124128059412
        or reaction.message.channel.id == 873657874910412830
        or reaction.message.channel.id == 873940155109617755
        or reaction.message.channel.id == 872147016661213204
        or reaction.message.channel.id == 844604570716864542
        or reaction.message.channel.id == 864343255364927529
        or reaction.message.channel.id == 871770749545906177
        or reaction.message.channel.id == 873799551704760341
        or reaction.message.channel.id == 873461514592477237
        or reaction.message.channel.id == 870818262265516072
        or reaction.message.channel.id == 836721067178721340
        or reaction.message.channel.id == 873633578779566130
        or reaction.message.channel.id == 873808993745797130
        or reaction.message.channel.id == 874038447566884945
        or reaction.message.channel.id == 832587911529627658
        or reaction.message.channel.id == 870338367936659517
        or reaction.message.channel.id == 875773258740400198
        or reaction.message.channel.id == 863869599236489236
        or reaction.message.channel.id == 863860086337830912
        or reaction.message.channel.id == 822755849407168525
    ):

        if reaction.emoji == "🎉":
            if reaction.message.id not in ban:
                if "bot" not in reaction.message.content.lower():
                    if reaction.message.author.id == 617037497574359050:
                        print(f"Detected 🎉 giveaway! channel: {reaction.message.guild.name} - room id: {reaction.message.channel.id} - room name: {reaction.message.channel.name}")
                        #await asyncio.sleep(round(randint(1,3)))
                        await asyncio.sleep(round(randint(15,30)))
                        #quick - await asyncio.sleep(round(randint(0,1)))
                        await reaction.message.add_reaction("🎉")
                        ban.append(reaction.message.id)
                        print(f"Reacted 🎉! channel: {reaction.message.guild.name} - room id: {reaction.message.channel.id} - room name: {reaction.message.channel.name}")
                else:
                    print(f"PanicSleep: {reaction.message.content.lower()}")
                    time.sleep(60)
                    print("PanicSleepEnd")
                    return
            else:
                print(f"Already reacted!")

        if reaction.emoji == "🍌":
            if reaction.message.id not in ban:
                if "bot" not in reaction.message.content.lower():
                    if reaction.message.author.id == 617037497574359050:
                        print(f"Detected 🍌 giveaway! channel: {reaction.message.guild.name} - room id: {reaction.message.channel.id} - room name: {reaction.message.channel.name}")
                        #await asyncio.sleep(round(randint(1,3)))
                        await asyncio.sleep(round(randint(15,30)))
                        #quick - await asyncio.sleep(round(randint(0,1)))
                        await reaction.message.add_reaction("🍌")
                        ban.append(reaction.message.id)
                        print(f"Reacted 🍌! channel: {reaction.message.guild.name} - room id: {reaction.message.channel.id} - room name: {reaction.message.channel.name}")
                else:
                    print(f"PanicSleep: {reaction.message.content.lower()}")
                    time.sleep(60)
                    print("PanicSleepEnd")
                    return
            else:
                print(f"Already reacted!")

        if reaction.emoji == "🍆":
            if reaction.message.id not in ban:
                if "bot" not in reaction.message.content.lower():
                    if reaction.message.author.id == 617037497574359050:
                        print(f"Detected 🍆 giveaway! channel: {reaction.message.guild.name} - room id: {reaction.message.channel.id} - room name: {reaction.message.channel.name}")
                        #await asyncio.sleep(round(randint(1,3)))
                        await asyncio.sleep(round(randint(15,30)))
                        #quick - await asyncio.sleep(round(randint(0,1)))
                        await reaction.message.add_reaction("🍆")
                        ban.append(reaction.message.id)
                        print(f"Reacted 🍆! channel: {reaction.message.guild.name} - room id: {reaction.message.channel.id} - room name: {reaction.message.channel.name}")
                else:
                    print(f"PanicSleep: {reaction.message.content.lower()}")
                    time.sleep(60)
                    print("PanicSleepEnd")
                    return
            else:
                print(f"Already reacted!")

        if reaction.emoji == "🇵🇱":
            if reaction.message.id not in ban:
                if "bot" not in reaction.message.content.lower():
                    if reaction.message.author.id == 617037497574359050:
                        print(f"Detected 🇵🇱 giveaway! channel: {reaction.message.guild.name} - room id: {reaction.message.channel.id} - room name: {reaction.message.channel.name}")
                        #await asyncio.sleep(round(randint(1,3)))
                        await asyncio.sleep(round(randint(15,30)))
                        #quick - await asyncio.sleep(round(randint(0,1)))
                        await reaction.message.add_reaction("🇵🇱")
                        ban.append(reaction.message.id)
                        print(f"Reacted 🇵🇱! channel: {reaction.message.guild.name} - room id: {reaction.message.channel.id} - room name: {reaction.message.channel.name}")
                else:
                    print(f"PanicSleep: {reaction.message.content.lower()}")
                    time.sleep(60)
                    print("PanicSleepEnd")
                    return
            else:
                print(f"Already reacted!")
                
@client.event
async def on_message(message):
    if "bot" in message.content.lower():
        print(f"PanicSleep: {message.content.lower()}")
        time.sleep(60)
        print("PanicSleepEnd")
        return

    if username in message.content.lower():
        print(f"PanicSleep: {message.content.lower()}")
        time.sleep(600)
        print("PanicSleepEnd")
        return

    if message.content.startswith("$phrasedrop"):
        c.can = True
        await asyncio.sleep(60)
        c.can = False

    if message.content.startswith("$airdrop"):
        #val = randrange(21)
        #if val == 7:
            await asyncio.sleep(randint(5,15))
            #await message.channel.send(choice(ty))

    if message.content.startswith("!airdrop"):
        #val = randrange(21)
        #if val == 7:
            await asyncio.sleep(randint(5,15))
            #await message.channel.send(choice(ty))

    if str(c.cache) not in c.sent:
        if message.author.id != 0:
            if c.cache == message.content.lower():
                if str(c.cache) not in c.sent:
                    await asyncio.sleep(randint(0,3))
                    if c.cache != None and c.cache != "":
                        if c.can:
                            print(f"c.cache = {c.cache}")
                            c.can = False
                            await message.channel.send(f"{c.cache}")
                            print(f"Sent c.cache")
                            time.sleep(10)
                            c.sent.append(c.cache)
                            c.cache = None
                            return


    if message.author.id != 1:
        if message.author.id != 0:
            if message.content.lower().startswith("$") == False:
                await asyncio.sleep(0.5)
                if message.reactions != []:
                    c.cache = message.content.lower()
                    print(f"c.cache = {c.cache}")
                else:
                    try:
                        x = float(message.content)
                    except:
                        pass
                    else:
                        c.cache = message.content

if get('https://api.ipify.org').text != str(ip):
    client.run(TOKEN_AUTH, bot=False)
else:
    print("HOME IP")
    quit()
