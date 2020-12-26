import sys, discord, os, base64
sys.path.insert(0,"")  # my path top secret ^-^
import SciModule_Py
from github import Github
from pprint import pprint



#constant
client = discord.Client()
username = "MuscleBrain"
g = Github()



pk = SciModule_Py.Physics_Modules.kinemic() 



def fileExist(Module):
    Module += "_Modules.py"
    path = f"" # my path top secret ^-^
    return os.path.isfile(path) 



@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$'):         # if $
        user_input = message.content.split()
        subject = user_input[1]
        if fileExist(subject) == True:    # ex: Math or Physics
            q_num = username[2]                 # ex: func1 or func2
            q_kno = user_input[3]             # ex: [1,2,3,4]
            answer = exec(f"{subject}._{q_num}_({q_kno})")
            await message.channel.send(answer)      # result 
client.run('') # robot key  top secret ^-^











