

def HangMan():
    import random, time
    center_body_parts = ["O","/","|","\\","(",")", " "]   #init
    body_part = [" ", " ", " ", " ", " ", " ", " "]        # init
    body_parts_refer = ["O","/","|","\\","(",")", " "]       # init
    down_elem = ["-","-","-","-","-","-","-","-","-","-"," "]  # init

    def first_screen():
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\nWelcome to HangMan; l am MuscleBrain; let's have some fun!\n\n")
        # time.sleep(1)
        # print("Starts in----------3\n\n")
        # time.sleep(1)
        # print("Wait-----------2\n\n")
        # time.sleep(1)
        # print("Okey-------1\n\n")
        # time.sleep(1)
        # print("Start--0\n\n")

    def screen_graph():
        up_right_sentence = ""      #init 
        down_right_nice_guess = ["","","","","",""]  # init
        down_right_sorry = ["","","","","",""]          # init
        down_right_capital_letter = ["","","","","",""]  # init
        up_right_sentence_num = ["Zero","One","Two","Three","Four","Five","Six"] # init


        def change_center_part():
            center_body_parts[false_time - 1] = user_guess_input    
        def change_sign_to_letter():
            for ii in range(0,len(word)):
                try:
                    down_elem[word.index(user_guess_input,ii,ii+1)] = user_guess_input
                except:
                    pass

        ################################################################


        if is_correct_answer == True:
            down_right_nice_guess = ["+~~~~~~~~~~~~~~~~~~~+" , "|      Correct      |" , "| \"Nice guess man\"  |" , "| \"you are so good\" |" , "+~~~~~~~~~~~~~~~~~~~+"]
            up_right_sentence = "\"Given me your guess; (A captital letter); {up_right_sentence_num[6-false_time]} choise left.\"" 
            change_sign_to_letter()

        elif is_correct_answer == False:
            down_right_sorry = ["+~~~~~~~~~~~~~~~~~~~+" , "|       Sorry       |" , "| \"That\'s okey men\" |" , "| \"Try another one\" |" , "+~~~~~~~~~~~~~~~~~~~+"]
            up_right_sentence = f"\"Given me your guess; (A captital letter); {up_right_sentence_num[6-false_time]} choise left.\""
            change_center_part() 
            body_part[false_time-1] = body_parts_refer[false_time-1]

        elif is_correct_answer == None:
            up_right_sentence ="\"Come on baby, capital letter please; you know that, do you?\""
            down_right_capital_letter = ["+~~~~~~~~~~~~~~~~~~~+" , "|  capital letter   |" , "|(-(-.(-.-).-)-).-) |" , "|                   |" , "+~~~~~~~~~~~~~~~~~~~+"]

        ##############################################################


        down_elems_final_list = [   f"={down_elem[0]}=" * (len(word)>=4),
                                    f"={down_elem[1]}=" * (len(word)>=4),
                                    f"={down_elem[2]}=" * (len(word)>=4),
                                    f"={down_elem[3]}=" * (len(word)>=4),
                                    f"={down_elem[4]}=" * (len(word)>=5),
                                    f"={down_elem[5]}=" * (len(word)>=6),
                                    f"={down_elem[6]}=" * (len(word)>=7),
                                    f"={down_elem[7]}=" * (len(word)>=8),
                                    f"={down_elem[8]}=" * (len(word)>=9),
                                    f"={down_elem[9]}=" * (len(word)>=10),
                                ]             

        down_left_enter_key = "                                        "
        for ii in range(len(word)):
            if word[ii] != down_elem[ii]:
                break 
            if ii == len(word)-1:
                down_left_enter_key = "Type Enter Key to celebrate your SUCCESS"
                

        print(f"""
        =============================================================================================
                                                                                               
        <Exit>                                                                             
                ++=======++                                {up_right_sentence}
                ||        |             +-----+                                                                          
                ||        {body_part[0]}             |  {center_body_parts[0]}  |                                                          
                ||       {body_part[1]}{body_part[2]}{body_part[3]}            | {center_body_parts[1]}{center_body_parts[2]}{center_body_parts[3]} |                                                                    
                ||       {body_part[4]} {body_part[5]}            | {center_body_parts[4]} {center_body_parts[5]} |                                                                    
                ||                      +-----+                                                             
                ||                                                                                   
                ||                                                                                   
                ||                                                                                   
            --------------                                                                           
                                                                               {down_right_nice_guess[0]}{down_right_sorry[0]}{down_right_capital_letter[0]} 
                                                                               {down_right_nice_guess[1]}{down_right_sorry[1]}{down_right_capital_letter[1]} 
                                                                               {down_right_nice_guess[2]}{down_right_sorry[2]}{down_right_capital_letter[2]} 
                                                                               {down_right_nice_guess[3]}{down_right_sorry[3]}{down_right_capital_letter[3]} 
            {down_left_enter_key}                           {down_right_nice_guess[4]}{down_right_sorry[4]}{down_right_capital_letter[4]} 
                                                                                            0        
                                                                                           /|\       
                                                                                           ( )
                   {down_elems_final_list[0]}   {down_elems_final_list[1]}   {down_elems_final_list[2]}   {down_elems_final_list[3]}   {down_elems_final_list[4]}   {down_elems_final_list[5]}   {down_elems_final_list[6]}   {down_elems_final_list[7]}   {down_elems_final_list[8]}   {down_elems_final_list[9]}                      
        =============================================================================================
            """)

            
        
    def get_newWord():
        global alpha_list, word
        alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        word = ""

        for a in range(random.randint(4,10)):
            word += alpha_list[random.randint(0,25)]
        

    first_screen()

    exit_or_keep = "keep"  #init
    false_time = 0  #init
    is_correct_answer = True  #init
    if_win = False
                                                                        

    get_newWord()

    screen_graph()
    user_guess_input = str(input(" "))  

    while exit_or_keep != "exit":
        

        for ii in range(len(word)):
            if word[ii] != down_elem[ii]:
                break 
            if ii == len(word)-1:
                if_win = True




        if false_time == 6 or if_win == True:
            
            if false_time == 6:
                print("Hi, want to play one more time? (\"exit\" fot leaving)(\"keep\" for keeping play)")

            elif if_win == True:
                print("Congratulation!!!!! You win the game ! You are so good !")
                print("So, do you want to play one more time? (\"exit\" fot leaving)(\"keep\" for keeping play)")

            user_if_stay_input = input()

            while True:
                if user_if_stay_input == "exit":
                    exit_or_keep = "exit"
                    break

                elif user_if_stay_input == "keep":
                                                                                            #if_play_again = True
                    center_body_parts = ["O","/","|","\\","(",")","."]   #init
                    body_part = [" ", " ", " ", " ", " ", " "," "]        # init
                    body_parts_refer = ["O","/","|","\\","(",")"]       # init
                    down_elem = ["-","-","-","-","-","-","-","-","-","-"]  # init  
                    false_time = 0 # init
                    if_win = False
                    get_newWord()
                    break

                else:
                    print("E ooooh, l can only read \"exit\" or \"keep\"; what is your choise again?")
                    user_if_stay_input = input("(\"exit\" fot leaving)(\"keep\" for keeping play)")


        if exit_or_keep == "exit":
            break
        if user_guess_input not in word and user_guess_input in alpha_list: # wrong guess
            is_correct_answer = False
            false_time += 1
            screen_graph()
            user_guess_input = str(input(" "))    

        elif user_guess_input in word: # right guess

            screen_graph()
            user_guess_input = str(input(" "))  
            

        elif user_guess_input not in alpha_list: # type not cappitle letter
            is_correct_answer = None
            screen_graph()
            user_guess_input = str(input(" "))    

        elif user_guess_input == "exit": # user want to leave
            exit_or_keep = "exit"
            break

    print("See you man; hope you enjoy the game!")

HangMan()
