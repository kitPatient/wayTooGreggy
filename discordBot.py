from asyncio.windows_events import NULL
from email.message import Message
import discord
import json
import random

debugMode = False

'''---------COMMON VARIABLES AND LINKS---------'''
#Assigns the suffix used for the commands
suffix = "$"

#What displays the bot as currently playing
currentlyPlaying = "Not Too Greggy"
 
#Link to Github Repo
linkREPO = "https://github.com/kitPatient/GregsJourney"

#Links to images
linkGTNH = "https://cdn.discordapp.com/attachments/963701404843794432/972601235511328858/unknown.png"
linkGREGTECHLOGO = "https://static.wikia.nocookie.net/ftb_gamepedia/images/8/82/Modicon_GregTech_Community_Edition.png"

#User ID's
IDnot0the0flash = 499704705111556108
IDguristic = 738112885196062813

#Emojis
emojiA = '🇦'
emojiB = '🇧'

#Colors
normalColor = 0xFF5733

#DirectoryLinks
dirCommandHelper = "command_helper.json"
dirVersion = "version.json"
dirPoll = "json_poll.json"

#load the client
client = discord.Client(activity=discord.Game(name=currentlyPlaying))

'''---------COMMON FUNCTIONS---------'''

def getBotToken():
	if(debugMode):
		print("Loading Token!")
	x = open("botToken.token","r")
	xr = x.read()
	x.close()
	return xr

def loadJsonData(filename):
    _a = open(filename,"r")
    _ar = _a.read()
    _aj = json.loads(_ar)
    _a.close()
    return _aj

def dumpJsonData(filename, data, indent = 2):
    _a = open(filename,"w")
    _as = json.dumps(data,indent = indent)
    _a.write(_as)
    _a.close()
    
    #jsonFile = open("json_poll.json", "w")
	#jsonString = json.dumps(dict,indent=2)
	#jsonFile.write(jsonString)
	#jsonFile.close()

#Same as dumpJsonData
#def updateJson(filename,data,indent=2):
    #jsonFile = open(filename,"w")
    #jsonString = json.dumps(data,indent=indent)
    #jsonFile.write(jsonString)
    #jsonFile.close()
    
def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last,start)
        return s[start:end]
    except ValueError:
        return ""

#def saveDict(dict):
    #dumpJsonData("json-poll.json",dict)
    #jsonFile = open("json_poll.json", "w")
    #jsonString = json.dumps(dict,indent=2)
    #jsonFile.write(jsonString)
    #jsonFile.close()

#def updateVersion(newVersion):
	#jsonFile = open("version.json", "w")
	#x = {"version": newVersion}
	#print(x)
	#jsonString = json.dumps(x,indent=2)
	#print(jsonString)
	#jsonFile.write(jsonString)
	#print(jsonString)
	#jsonFile.close()
 
async def addABReactions(message):
    await message.add_reaction(emojiA)
    await message.add_reaction(emojiB)

async def Mesage(message, response):
    return await message.channel.send(response)

async def EmbedMessage(message,response):
    return await message.channel.send(embed=response)

async def EmbededWthPic(message, url, color=normalColor):
    x = discord.Embed(color=color)
    x.set_image(url=url)
    return await EmbedMessage(message,x)


#Reloads The Help Commands each time, allows for changing
#the .json an it come up in the bot, without stopping the bot
def loadHelpEmbed(color = normalColor):
    NcommandHelp = loadJsonData(dirCommandHelper)
    NCcommandHelp = NcommandHelp["commands"]
    x = discord.Embed(title="Command Display",color=color)
    x.set_thumbnail(url=linkGREGTECHLOGO)
    x.add_field(name="$hello", value=NCcommandHelp["hello"], inline=False)
    x.add_field(name="$gtnh", value=NCcommandHelp["gtnh"], inline=False)
    x.add_field(name="$poll", value=NCcommandHelp["poll"], inline=False)
    x.add_field(name="$link", value=NCcommandHelp["link"], inline=False)
    x.add_field(name="$newPoll", value=NCcommandHelp["newPoll"], inline=False)
    x.add_field(name="$flip", value=NCcommandHelp["flip"], inline=False)
    x.add_field(name="$status", value=NCcommandHelp["status"], inline=False)
    x.add_field(name="$setStatus", value=NCcommandHelp["setStatus"],inline=False)
    x.add_field(name="$help", value=NCcommandHelp["help"], inline=False)
    #mes = await message.channel.send(embed = x)
    return x

'''---------START OF BOT---------'''

botToken = getBotToken()

if(debugMode):
	print(botToken)

#Loads Commands as a json to commandHelp
#commandHelpL = open("command_helper.json", "r")
#commandHelpg = commandHelpL.read()
#commandHelp = json.loads(commandHelpg)
#commandHelpL.close()

#commandHelp = loadJsonData("command_helper.json")

@client.event
async def on_message_edit(before, after):
    
    if (before.author or after.author == client.user):
        return
    else:
        print('Old Message by: {0.author.display_name}, With Message: {0.content}'.format(before))
        print('New Message: {0.content}'.format(after))

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    x = loadJsonData("commands.json")
    mess = message.content
    #mess = suffix+mess
    
    if mess.startswith(suffix):
        mess = mess[1:]
    
    mess = mess.lower()
    if debugMode:
        print(mess)
    
    try:
        command = x[mess]
        if debugMode:
            await Mesage(message, "COMMAND")
            print("COMMAND")
            await Mesage(message, command)
            print(command)
            await Mesage(message, "------------------")
            print("------")
            await Mesage(message, "MESSAGE")
            print("MESSAGE")
            await Mesage(message, mess)
            print(mess)
        #
        if x[mess]["actionType"] == "basicResponse":
            #print("Basic Response Action")
            await Mesage(message,x[mess]["response"])
        
    except KeyError:
        if debugMode:
            print("ERROR: COMMAND NOT FOUND")
        return
    
    
    
'''
    if message.content.startswith('{0}hello'.format(suffix)):
        await Mesage(message, "Hello")

    if message.content.startswith('{0}gtnh'.format(suffix)):
        await EmbededWthPic(message,linkGTNH)
        
    if message.content.startswith('{0}epoll1'.format(suffix)):
        not0the0flash = await client.fetch_user(IDnot0the0flash)
        if message.author == not0the0flash:
            pollData = loadJsonData(dirPoll)
            await Mesage(message, pollData["a"])
            #with open('json_poll.json') as json_file:
                #data = json.load(json_file)
                #await message.channel.send(data["a"])
                #json_file.close()

    if message.content.startswith('{0}poll'.format(suffix)):
        #not0the0flash = await client.fetch_user(IDnot0the0flash)
        #Gu = await client.fetch_user(IDguristic)
        #if message.author == not0the0flash or Gu:     
        
        pollData = loadJsonData(dirPoll)
            
        x = discord.Embed(title=pollData["title"],color=normalColor)
        x.set_thumbnail(url=linkGREGTECHLOGO)
        x.add_field(name="Option A: ", value=pollData["a"], inline=True)
        x.add_field(name="Option B: ", value=pollData["b"], inline=True)
        mes = await message.channel.send(embed = x)
        await addABReactions(mes)
            
            #with open('json_poll.json') as json_file:
                #data = json.load(json_file)
                #x = discord.Embed(title=data["title"],color=0xFF5733)
                #x.set_thumbnail(url=linkGREGTECHLOGO)
                #x.add_field(name="Option A: ", value=data["a"], inline=True)
                #x.add_field(name="Option B: ", value=data["b"], inline=True)
                #mes = await message.channel.send(embed = x)
                #await addABReactions(mes)
                #json_file.close()

    if message.content.startswith('{0}link'.format(suffix)):
        await Mesage(message, linkREPO)
        
    if message.content.startswith('how do i craft '):
        await Mesage(message,"Use Jei. You Idiot!")

    if message.content.startswith('how do i use channels'):
        await Mesage(message,"I don't know google it or something")

    if message.content.startswith('E'):
        await Mesage(message,"E")
        
    if message.content.startswith('nice'):
        await Mesage(message, "nice")
        
    if message.content.startswith('{0}flip'.format(suffix)):
        x = random.randint(1,2)
        await message.channel.send(x)
        
    if message.content.startswith('Bot should '):
        x = random.randint(1,2)
        if x == 1:
            await Mesage(message,"Yes")
            return
        else:
            await Mesage(message,"No")
                     
    if message.content.startswith('{0}status'.format(suffix)):
        #versionj = open("version.json", "r")
        #versionr = versionj.read()
        #version = json.loads(versionr)
        #versionj.close()
        
        version = loadJsonData(dirVersion)
        
        #print(version)
        await message.channel.send(version["version"])
        
    if message.content.startswith('{0}newPoll '.format(suffix)):
        text = message.content
        if len(text) > 8:
            result = find_between(text[8:],"(",")")
            if len(result)>6:
                lists = result.split(",")
                if len(lists)==3:
                    newPoll = {"title":lists[0],"a":lists[1],"b":lists[2]}
                    dumpJsonData(dirPoll,newPoll)
                    #saveDict(newPoll)
                    await message.channel.send("Poll Created Successfully!")
                    
    if message.content.startswith("{0}setStatus ".format(suffix)):
        text = message.content
        if len(text)>10:
            result = find_between(text[10:],"(",")")
            #updateVersion(result)
            versionData = {"version": result}
            dumpJsonData(dirVersion, versionData)
            await message.channel.send("Status Set to: " + result)
            
    if message.content.startswith('{0}help'.format(suffix)):
        
        #x = discord.Embed(title="Command Display",color=0xFF5733)
        #x.set_thumbnail(url=linkGREGTECHLOGO)
        #x.add_field(name="$hello", value=commandHelp["commands"]["hello"], inline=False)
        #x.add_field(name="$gtnh", value=commandHelp["commands"]["gtnh"], inline=False)
        #x.add_field(name="$poll", value=commandHelp["commands"]["poll"], inline=False)
        #x.add_field(name="$link", value=commandHelp["commands"]["link"], inline=False)
        #x.add_field(name="$newPoll", value=commandHelp["commands"]["newPoll"], inline=False)
        #x.add_field(name="$flip", value=commandHelp["commands"]["flip"], inline=False)
        #x.add_field(name="$status", value=commandHelp["commands"]["status"], inline=False)
        #x.add_field(name="$setStatus", value=commandHelp["commands"]["setStatus"],inline=False)
        #x.add_field(name="$help", value=commandHelp["commands"]["help"], inline=False)
        
        helpEmbed = loadHelpEmbed()
        
        mes = await message.channel.send(embed = helpEmbed)
'''
#Run the client
client.run(botToken)