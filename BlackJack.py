#Libraries needed
from time import sleep
import random
import csv #file type
import sys #allow to quit from cmd
#rules
print("""
--------------- RULES ---------------
\n1: Each 'player' draws 2 cards
2: Players get three options, these are to either stick, twist or fold
\t-Sticking takes your score from the value of the cards in your hand
\t-Twisting adds another card to the your hand
\t-Folding throws your hand away and results in a score of 0
3: Players go bust when their cards/score exceed 21
\n--------------- RULES --------------- \n
""")

class hand():
    def __init__(self,texture_pack):
        self.hand = []
        self.change_texture_pack(texture_pack)
        

    def change_texture_pack(self,texture_pack):
        #Changes texture pack one is provided, else reverts to default
        if isinstance(texture_pack,tuple):
            self.texture_pack = texture_pack # if other texture packs are there, it will print the hand in all of the different types of textures
        else:
            self.texture_pack = (3,
                "/----\\",
                "|    |",
                "| ","|",
                "|    |",
                "\----/") #ability to add new texture packs if needed
    
    def __render_card(self,card_code):
        #Private - Renders an individual card using the texture pack
        if card_code[0:2] == "11":
            card_code = "J"+card_code[2:]
        elif card_code[0:2] == "12":
            card_code = "Q"+card_code[2:]
        elif card_code[0:2] == "13":
            card_code = "K"+card_code[2:]
        elif card_code[0] == "1" and card_code[1] != "0":
            card_code = "A"+card_code[1:]

        if card_code[0:2] != "10":
            card_code += " "

        #Inserts the appropriate card code into the ASCII image
        cc_pos = self.texture_pack[0]
        render_list = list(self.texture_pack)
        del render_list[0]
        cc_row = str(render_list[cc_pos-1] + card_code + render_list[cc_pos])
        del render_list[cc_pos-1:cc_pos+1]
        render_list.insert(cc_pos-1,cc_row)
        return render_list

    def render_hand(self):
        """Renders all of the cards currently in the hand"""
        render_string = ""
        hand_list = []
        for card in self.hand:
            hand_list.append(self.__render_card(card))
        for i in range(len(self.texture_pack)-2): #Number of rows in texture
            for card in hand_list:
                render_string += card[i] + "  "
            render_string += "\n"
        return render_string
            
    def draw(self,num_times):
        #Draws a given number of cards into the hand
        global deck
        for i in range(num_times):
            rand_ind = random.randint(0,len(deck)-1)
            self.hand.append(deck[rand_ind])
            del deck[rand_ind]
        return self.hand

    def score(self):
        possible_scores = [0] #keep track of aces
        for card_code in self.hand: #goes through hand
            #Calculate score
            if card_code[1] not in ["D","C","S","H"]: #checks if index 1 is a letter, if not, it is a 10 (10 is only 2 digit number in a deck)
                possible_score = 10
            elif card_code[0] != "1": #if card not ace, make score that card's value
                possible_score = int(card_code[0]) 
            elif card_code[0] == "1": #if card is ace
                possible_scores.extend(possible_scores) #extends list to make ace equal to 11 and 1
                #Adds 1 to half of the list and 11 to the other 
                for i in range(0,int(0.5*len(possible_scores))): #loop through first half of list (1st list)
                    possible_scores[i] += 1 #ace = 1 in first list
                for i in range(int(0.5*len(possible_scores)),len(possible_scores)):
                    possible_scores[i] += 11 #ace = 11 in second list
                possible_score = 0
            else:
                print("Error has occurred")
            #Adds the score to total
            if possible_score != 0:
                for score in range(len(possible_scores)):
                    possible_scores[score] += possible_score
        possible_scores.sort() #sorts the possible scores from lowest to highest
        if possible_scores[0] > 21: #if the 1st number, i.e. lowest possible score is above 21
            return possible_scores[0] #return the number for bust as if the lowest is above 21, all of them will be
        for i in range(len(possible_scores)): #checks if scores are above 21
            if possible_scores[i] > 21: #if any are above 21
                return possible_scores[i-1] #return the score before because that will be the score below 21
        return possible_scores.pop()

    def blackjack(self): #checks for blackjack (my custom rules)
        card_scores = []
        for i in self.hand: # i = card score in hand e.g. 12C (Queen clubs)/7C(7 clubs)
            for x in i: # seperate each value of i e.g. [1,2,C]
                card_scores.append(x) # add each value to new list 
        if card_scores[1] == '1' and card_scores[3] == '1': # if second digit e.g. 1[1] is 1 and 3rd list index == 1 (ace) it's blackjack
            return True
        elif card_scores[1] == '2' and card_scores[3] == '1': # same for all of these combinations
            return True
        elif card_scores[1] == '3' and card_scores[3] == '1':
            return True
        elif card_scores[0] == '1' and card_scores[3] == '1':
            return True
        elif card_scores[0] == '1' and card_scores[3] == '2':
            return True
        elif card_scores[0] == '1' and card_scores[3] == '3':
            return True
           
            




card_format = (3, #3 is needed to format the card correctly
                "/----\\",
                "|    |",
                "| ","|",
                "|    |",
                "\----/")

#Generates deck of cards
deck = []

for pack_of_cards in range(1):
    for suit in ["D","C","S","H"]:
        for num in range(1,14):
            deck.append(str(num)+suit)
        
    def name_validator():
        name_list = []
        while True:
          try:
            name = str(input("Please enter your first name: ")).capitalize()
            if (len(name) > 2 and name.isalpha() and (len(name) < 10)): #name needs to be greater than 2 characters, less than 10
                name_list.append(name)
                break
            else:
                raise TypeError #if anything other than ^, raise TypeError
          except TypeError: #if TypeError
            print("First name only please (max length 10)") #print message and return to while loop
            continue
        return name_list[0] #to get name out of list


    
    def game(user_name):
        names = ["Riccardo","Karan","Niccolò","Nam","Lewis","Vasu","Jake","Finlay","Chris","Billy","Orin"]
        player1_name = random.choice(names)
        names.remove(player1_name)
        player2_name = random.choice(names)
        names.remove(player2_name)

        #new object for each hand
        user_hand = hand(card_format)
        player1_hand = hand(card_format)
        player2_hand = hand(card_format) 
        dealer_hand = hand(card_format)
        
        scores = {
            user_name:0,
            player1_name:0,
            player2_name:0,
            "Dealer":0
            }
        #create each player's starting hand
        u_draw = user_hand.draw(2)
        p1_start_hand = player1_hand.draw(2)
        p2_start_hand = player2_hand.draw(2)
        d_hand = dealer_hand.draw(2)
        
        print("\nThe cards are being dealt\n")
        sleep(1)
        #USER SECTION
        print("  You Drew \n")
        print(user_hand.render_hand())
        sleep(1)
        if user_hand.score() == 21 and user_hand.blackjack() == True:
            print ("You got BlackJack!")
            scores[user_name] = user_hand.score()
            sleep(1)
        elif user_hand.score() == 21:
            print("Congratulations, you got 21")
            scores[user_name] = user_hand.score()
        else:
            print ("Your score is",user_hand.score())
            sleep(1)
        while user_hand.score() < 21:
            s_t_f = input("\nThe dealer has asked whether you would like to stick, twist or fold (s,t,f): ").lower()
            if s_t_f == "s":
                sleep(1.5)
                print ("\nYou have indicated to the dealer you are sticking with your current hand...")
                sleep(1)
                print("\nYour final score this round is:",user_hand.score())
                scores[user_name] = user_hand.score()
                break
            elif s_t_f == "t":
                print ("\nTwisting....")
                sleep(1)
                u_draw + user_hand.draw(1)
                if user_hand.score() == 21:
                    print(user_hand.render_hand())
                    print ("You got 21, nice one!")
                    scores[user_name] = user_hand.score()
                elif user_hand.score() < 21:
                    print(user_hand.render_hand())
                    print("\nYour score is now", user_hand.score())
                elif user_hand.score() > 21:
                    print(user_hand.render_hand())
                    print ("\nYou went bust with", user_hand.score())
                    scores[user_name] = 0
                    break
                else:
                    print("Something went wrong")
                while user_hand.score() < 21: #score must be below 21 to twist again
                    twist_again = input("\nTwist again? (y/n): ").lower()
                    if twist_again == "y":
                        print("\nTwisting...")
                        sleep(1)
                        u_draw + user_hand.draw(1)
                        print(user_hand.render_hand())
                        if len(u_draw) == 5 and user_hand.score() <= 21:
                            print("5 Card Trick, Congratulations")
                            scores[user_name] = 21
                            break
                        elif user_hand.score() < 21:
                            print("\nYour score is now", user_hand.score())
                        elif user_hand.score() == 21:
                            print ("You got 21, nice one!")
                            print(user_hand.render_hand())
                            scores[user_name] = 21
                        elif user_hand.score() > 21:
                            print ("\nYou busted with", user_hand.score())
                            scores[user_name] = 0
                    elif twist_again == "n":
                            print("Your final score is", user_hand.score(), "for this round")
                            scores[user_name] = user_hand.score()
                            break
                    else:
                        print("Invalid Input")
                    continue
                break
                
                if user_hand.score() > 21:
                    print ("\nYou scored", user_hand.score(), "resulting in an automatic bust")
                    print(user_hand.render_hand())
            elif s_t_f == "f":
                print("\nYou have indicated that you would like to fold with", user_hand.score(),"\n\n(You are now out of this round)")
                scores[user_name] = 0
                break

            else:
                print("\nInvalid input, please only enter s/t/f")
             #break out of while loop when this section ends
        
    #Player 1
        sleep(3)
        print("\n"+player1_name,"draws two cards")
        print (player1_hand.render_hand())
        sleep(2)
        if player1_hand.score() == 21 and player1_hand.blackjack() == True:
            (player1_name, "got Blackjack")
            scores[player1_name] = player1_hand.score()
        while player1_hand.score() < 17:
            p1_start_hand + player1_hand.draw(1)
            sleep(1)
            print (player1_name,"twists")
            print (player1_hand.render_hand())
        if player1_hand.score() >= 17 and player1_hand.score() <= 21:
            sleep(1)
            print ("\n"+player1_name,"is sticking with his hand")
            scores[player1_name] = player1_hand.score()
            print (player1_hand.render_hand())
        elif player1_hand.score() > 21:
            sleep(1)
            print (player1_name,"has gone bust")
        else:
            print("Something has gone wrong,",player1_name+"'s score will not be recorded this round")
        sleep(5)
        
    #Player 2
        sleep(3)
        print("\n"+player2_name,"draws two cards")
        print (player2_hand.render_hand())
        sleep(2)
        if player2_hand.score() == 21 and player2_hand.blackjack() == True:
            print(player2_name, "got Blackjack")
            scores[player2_name] = player2_hand.score()
        while player2_hand.score() < 17:
            p2_start_hand + player2_hand.draw(1)
            sleep(1)
            print (player2_name,"twists")
            print (player2_hand.render_hand())
        if player2_hand.score() >= 17 and player2_hand.score() <= 21:
            sleep(1)
            print ("\n"+player2_name,"is sticking with his hand")
            scores[player2_name] = player2_hand.score()
            print (player2_hand.render_hand())
        elif player2_hand.score() > 21:
            sleep(1)
            print (player2_name,"has gone bust")
        else:
            print("Something has gone wrong,",player2_name+"'s score will not be recorded this round")

    #Dealer
        sleep(3)
        print("\nDealer draws two cards")
        print(dealer_hand.render_hand())
        if dealer_hand.score() == 21 and dealer_hand.blackjack() == True:
            print("The dealer got Blackjack")
            scores['Dealer'] = dealer_hand.score()
        while dealer_hand.score() < 17:
            d_hand + dealer_hand.draw(1) #twists
            sleep(1)
            print("Dealer twists")
            print(dealer_hand.render_hand())
        if dealer_hand.score() >= 17 and dealer_hand.score() <= 21:
            sleep(1)
            print("Dealer sticks")
            scores['Dealer'] = dealer_hand.score()
        elif dealer_hand.score() > 21:
            sleep(1)
            print("Dealer has gone bust")
            scores['Dealer'] = 0 
        else:
            print("Something has gone wrong, dealer loses this round")
        sleep(5)
        print("\n" *30) #clears screen to show results

        print ("\n\nGame has ended, let's see who has won")
        #prints the hands of all the players
        print("User's hand:")
        print(user_hand.render_hand())
        sleep(1.5)
        print (player1_name,"'s hand")
        print (player1_hand.render_hand())
        sleep(1.5)
        print (player2_name ,"'s hand")
        print (player2_hand.render_hand())
        print ("Dealer's hand")
        print (dealer_hand.render_hand())
        

        if scores['Dealer'] > scores[user_name]: #if dealer score is above user, dealer wins
            print("The Dealer has won this round\n")
        elif scores['Dealer'] < scores[user_name]: #if dealer score is below user's, user wins
            print("The Dealer has lost this round\n")
        elif scores['Dealer'] == scores[user_name]: #draw if dealer score = user score
            print("You drew with the dealer\n")

        score_list = []
        for i in scores: #loop through dictionary
            player_info = [] 
            player_info.append(i) #adds key to list
            player_info.append(scores[i])  #adds value of key to list
            score_list.append(player_info) #2D list to sort key and scores better
        score_list.sort(key=lambda x: x[1],reverse=True) #special function that sorts 2D lists


        #reset hand after game ends    
        user_hand = []
        player1_hand = []
        player2_hand = []
        player3_hand=[]

        print(file_score(score_list))
        return "\nThank you for playing my Blackjack game, why not play another?"

    def file_score(score_list):
    #writing to csv
        with open('Scoresheet.csv','a', newline ='') as file: #allows me to add my scores to the csv
            writer = csv.writer(file)
            name_score = []
            for i in range(len(score_list)):
                name_score.append(score_list[i][0])
                name_score.append(score_list[i][1])
            writer.writerow(name_score)
            file.close()
        return "\nScores were successfully added to the scoresheet"
        
        

    def leaderboard():
        #reads from csv file
        leader_board_score = [] # contains games
        with open('Scoresheet.csv') as score_file:
            csv_reader = csv.reader(score_file, delimiter=',') 
            for row in csv_reader: #looks at each row in csv file (game)
                leader_board_game = [] # list to hold every blackjack game in own list
                for score in range(1,len(row),2): #starts at index 1 and loops through the score of each person
                    leader_board_player = [] # list to record each player's stats in blackjack game
                    leader_board_player.append(row[score-1]) #adds name from file into list (-1 to record names instead of scores)
                    leader_board_player.append(row[score]) #adds score from file into list
                    leader_board_game.append(leader_board_player) #each time a player's name and their score is added, add to list to seperate from each player
                leader_board_score.append(leader_board_game)    #adds all players in the game to game list
            if len(leader_board_score) > 3:
                leader_board_score = leader_board_score[-3:] #if number of games > 3, take last 3 games printed
            score_file.close
    #formats scores
        print("\nThese are the three most recent games")
        for game in range(len(leader_board_score)): # goes through each game in 3D list
            print("\nGame "+ str(game+1) + ":") # adds 1 to game each time it loops
            for player in range(len(leader_board_score[game])):
                print(leader_board_score[game][player][0] + ": " + leader_board_score[game][player][1])    
        return leader_board_score
        


    def menu():
        print("Welcome to BlackJack \n")
        while True:
            choice = input("""
A: Play Game
B: Browse Leaderboard
Q: Quit

Please enter your choice: """).lower()

            if choice == "a":
                print(game(name_validator()))
            elif choice =="b":
                leaderboard()
            elif choice== "q":
                sys.exit
                break
            else:
                print("You must only select either A,B or Q")
                print("Please try again")
      


    def main():  
        menu()
    main()



