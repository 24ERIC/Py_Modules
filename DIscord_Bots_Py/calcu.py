import sys, discord
sys.path.insert(0,"")############# my path (top secret <^+^>)
import Physics_Modules , Math_Modules



client = discord.Client()
username = "MuscleBrain"
module_dict = {"Math":Math_Modules,"Physics":Physics_Modules}





@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    
    if message.content == "$":########################################## 1
        await message.channel.send(f"""
                                    \nHello, use \"$\" can wake me up <^+^>
                                    \nType "$ modules" to check all availble modules
                                    """)

    elif message.content == "$ modules":################################# 2
        modules_list = [i for i in module_dict.keys()]
        await message.channel.send(f"""
                                    \nAvailable for now:
                                    \n{modules_list}
                                    """)

    elif message.content.startswith('$'):     
        user_input = message.content.split()
        subject = user_input[1]

        if subject in module_dict.keys():
            if len(user_input) == 2 or int(user_input[2]) > len(module_dict[subject].func_list)-1:
                available_func = [i for i in range(1,len(module_dict[subject].func_list))]
                await message.channel.send(f"""
                                            \nThis is available function list:
                                            \n{available_func}
                                            """)

            elif len(user_input) == 3:
                await message.channel.send("""
                                            \nGive me your input:
                                            \nExample: "$ Math 1 [1,2,3]" 
                                            \n "[1,2,3]" is the input
                                            """)

            else:
                q_num, q_kno = user_input[2], eval(user_input[3])   
                answer = module_dict[subject].func_list[int(q_num)](q_kno)
                await message.channel.send(f"""
                                            \nYour answer :
                                            \n{answer}
                                            \n...............
                                            \nNote:(if you sure get right answer, then please ignore me)
                                            \nelse:
                                            \n--amount of your input may be more then function actually need
                                            \n--however, you may give right/wrong answer
                                            \n--your input may not on the order that function need
                                            """)  

        else:
            await message.channel.send("""
                                        \nOh no, this subject doesn't exit...
                                        \nMaybe try "$ modules" check all available modules
                                        """)
client.run('')############ my key (top secret <^+^>)












