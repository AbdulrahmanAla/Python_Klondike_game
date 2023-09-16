#############################################################################
# Project 10
#
# This project  will allow the user to play a simplified version of Klondike, with the program managing the game
#
# The deck of cards is shuffled and 28 cards are dealt into 7 columns to form the tableau and the last card placed in each column of the tableau is turned face up.
#
# The objective of the game is to move all 13 cards of each suit into the appropriate foundation.
#
#  To be moved into one of the foundations, the card must be the correct suit and rank: it must be the same suit as the other cards in that foundation The functionss will return True if the move was done successfully. Otherwise, it returns False
#
#the starting state of the game with the four data structures initialized as described in the document. All tableau cards face down except last cards in each column
#
# we would create stock_to_waste function that will check if the stock is empty and if it was true it wold append it to the waste
#
# the next function waste_to_tableau would move the card in waste to tableau if certain conditions were meet
#
# the next function waste_to_foundation would also move the cards from the waste to the founcation with speceifc conditions
#
# the next two functions are very simillar to the ones above, the first one would move the tableau to foundation with certain conditions and the other one would move the cards from tableau to tableau
#
# lastly in the main function we would print the menu and and promot for an input that would take the 
#
#############################################################################
from cards import Card, Deck

MENU ='''Prompt the user for an option and check that the input has the 
       form requested in the menu, printing an error message, if not.
       Return:
    TT s d: Move card from end of Tableau pile s to end of pile d.
    TF s d: Move card from end of Tableau pile s to Foundation d.
    WT d: Move card from Waste to Tableau pile d.
    WF d: Move card from Waste to Foundation pile d.
    SW : Move card from Stock to Waste.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game        
    '''

def initialize():
    '''This function returns the starting state of the game with the four data
structures initialized as described in the document. All tableau
cards face down except last cards in each column. '''
    tableau=[[],[],[],[],[],[],[]] # create a list of tableau that contain lists as number of colums
    deck_of_cards1= Deck()# create a varaible that has the cards using deck function
    deck_of_cards1.shuffle()# shuffle the cards
    foundation=[[],[],[],[]] # create a list of list for the foundation
    for o in range(32):# create a loop that would repeat the process multiple times to add the cards more than once in the column
        for i in range(1,8): # loop on the number of column
            for index, char in enumerate(tableau): # make an enumerate to get the number of the column
                if index+1 == i and len(char) != index+1: # check if the index matches with the index of column
                    tableau[index].append(deck_of_cards1.deal())# if the conditions hold true it would add the  
                    tableau[index][-1].flip_card()    #because in default the cards would be flipped up, this line would flip the card down     
    for  index1,char1 in enumerate(tableau):
        tableau[index1][-1].flip_card()# this line would get loop inside the columns and flip up the last card in each column
    stock = deck_of_cards1 
    waste= [deck_of_cards1.deal()]#this line would get the last card in and store it in the waste list
    return tableau, stock, foundation, waste
    
def display(tableau, stock, foundation, waste):
    """ display the game setup """
    stock_top_card = "empty"
    found_top_cards = ["empty","empty","empty","empty"]
    waste_top_card = "empty"
    if len(waste):
        waste_top_card = waste[-1] 
    if len(stock):
        stock_top_card = "XX" #stock[-1]
    for i in range(4):
        if len(foundation[i]):
            found_top_cards[i] = foundation[i][-1]
    print()
    print("{:5s} {:5s} \t\t\t\t\t {}".format("stock","waste","foundation"))
    print("\t\t\t\t     ",end = '')
    for i in range(4):
        print(" {:5d} ".format(i+1),end = '')
    print()
    print("{:5s} {:5s} \t\t\t\t".format(str(stock_top_card), str(waste_top_card)), end = "")
    for i in found_top_cards:
        print(" {:5s} ".format(str(i)), end = "")
    print()
    print()
    print()
    print()
    print("\t\t\t\t\t{}".format("tableau"))
    print("\t\t ", end = '')
    for i in range(7):
        print(" {:5d} ".format(i+1),end = '')
    print()
    # calculate length of longest tableau column
    max_length = max([len(stack) for stack in tableau])
    for i in range(max_length):
        print("\t\t    ",end = '')
        for tab_list in tableau:
            # print card if it exists, else print blank
            try:
                print(" {:5s} ".format(str(tab_list[i])), end = '')
            except IndexError:
                print(" {:5s} ".format(''), end = '')
        print()
    print()
    

def stock_to_waste( stock, waste ):
    '''This function would check if the stock is empty and if it was true it wold append it to the waste, the function will return
True if the move was done successfully. Otherwise, it returns False '''
    if len(stock) == 0: # check if the stock is empty or not and if it was empty it would return False
        return False
    else:

        waste.append(stock.deal()) # if the deal wasn't empty it would add it to the stock and return True
        return True
    
    
       
def waste_to_tableau( waste, tableau, t_num ):
    '''The function
will return True if the move is valid (False otherwise). If the move is valid, perform it.in addition it check if the  tableau list is empty and it would add cards from the waste to tableau with certain conditions'''
    if waste == []:
        return False
    elif tableau[t_num] == []: # check if the  tableau list is empty
         if waste[-1].rank() == 13: # check if the card is a king or not
             tableau[t_num].append(waste[-1]) # add the king to the tableau and return True
             waste.pop()
             return True
    elif tableau[t_num] != [] and (((tableau[t_num][-1].rank()) - 1) == waste[-1].rank() )  and (((tableau[t_num][-1].suit()==1 or tableau[t_num][-1].suit()==4) and (waste[-1].suit()==2 or waste[-1].suit()==3)) or ((tableau[t_num][-1].suit()==2 or tableau[t_num][-1].suit()==3) and (waste[-1].suit()==1 or waste[-1].suit()==4)) ) : # if the tableau is not empty  and the rank of the card was one higher than the one in the foundation and the shape and the color of the card is not the same it would add the card to the tableau and return True
        tableau[t_num].append(waste[-1])
        waste.pop() # delete the last value of the list
        return True
    
    return False # return False otherwise

def waste_to_foundation( waste, foundation, f_num ):
    '''The
function will return True if the move is valid (False otherwise). If the move is valid, perform
it. simillar to the one above this function will move the cards from waste to foundations if it were valid moves'''
    if foundation[f_num] == []: # check if the  foundation list is empty
         if waste[-1].rank() == 1: # check if the card is ace or not
             foundation[f_num].append(waste[-1]) # add the ace to the foundation and return True
             waste.pop() # delete the last value of the list
             return True
    elif foundation[f_num] != [] and ((foundation[f_num][-1].rank())+1 == waste[-1].rank() ) and ((foundation[f_num][-1].suit()) == waste[-1].suit() ):# if the foundation is not empty  and the rank of the card was one higher than the one in the foundation it would add the card to the foundation  and return True
        foundation[f_num].append(waste[-1])
        waste.pop() # delete the last value of the list
        return True
    
    return False # return False otherwise
    

def tableau_to_foundation( tableau, foundation, t_num, f_num ):
    '''The function will
return True if the move is valid (False otherwise). It will flip the new last card in the tableau column from the source if the card is not face up '''
    if foundation[f_num] == []: # check if the  foundation list is empty
         if tableau[t_num][-1].rank() == 1: # check if the card is ace or not
             foundation[f_num].append(tableau[t_num][-1]) # add the ace to the foundation and return True
             tableau[t_num].pop()
             if tableau[t_num] != [] and not tableau[t_num][-1].is_face_up():
                tableau[t_num][-1].flip_card()
             return True
    elif foundation[f_num] != [] and ((foundation[f_num][-1].rank())+1 == tableau[t_num][-1].rank() ) and ((foundation[f_num][-1].suit()) == tableau[t_num][-1].suit() ):# if the foundation is not empty  and the rank of the card was one higher than the one in the foundation it would add the card to the foundation  and return True
        foundation[f_num].append(tableau[t_num][-1])
        tableau[t_num].pop()
        if tableau[t_num] != [] and not tableau[t_num][-1].is_face_up():
                tableau[t_num][-1].flip_card()
            
        return True
    return False

def tableau_to_tableau( tableau, t_num1, t_num2 ):
    ''' The function will return True if the move is valid
(False otherwise). It would flip the new last card in the tableau column from the source if
the card is not face up'''
    if tableau[t_num2] == []: # check if the  tableau list is empty
        if tableau[t_num1][-1].rank() == 13: # check if the card is a king or not
            tableau[t_num2].append(tableau[t_num1][-1]) # add the king to the tableau and return True
            tableau[t_num1].pop()
            if tableau[t_num1] != [] and not tableau[t_num1][-1].is_face_up():
                tableau[t_num1][-1].flip_card()
            return True
    elif (((tableau[t_num1][-1].rank())+1 ) == (tableau[t_num2][-1].rank()))  and ((tableau[t_num1][-1].suit()) !=1 or tableau[t_num2][-1].suit() !=4 ) and ((tableau[t_num1][-1].suit()) !=2 or tableau[t_num2][-1].suit() !=3)  : # if the tableau is not empty  and the rank of the card was one higher than the one in the foundation and the shape and the color of the card is not the same it would add the card to the tableau and return True
        tableau[t_num2].append(tableau[t_num1][-1])
        tableau[t_num1].pop()
        if tableau[t_num1] != [] and not tableau[t_num1][-1].is_face_up():
                tableau[t_num1][-1].flip_card()
        return True
        
        
    
    return False # return False otherwise

    
    
def check_win (stock, waste, foundation, tableau):
    ''' This function checks if the game is in a winning configuration and returns True if the game is in a winning state: all cards are in the foundation, stock is empty,
waste is empty and tableau is empty. Otherwise, return False.
'''
    return True if len(stock) == 0 and waste == [] and tableau == [[],[],[],[],[],[],[]] else False # check if the waste and the stock and the tableau is empty then it would return True, otherwise it would return False

def parse_option(in_str):
    '''Prompt the user for an option and check that the input has the 
           form requested in the menu, printing an error message, if not.
           Return:
        TT s d: Move card from end of Tableau pile s to end of pile d.
        TF s d: Move card from end of Tableau pile s to Foundation d.
        WT d: Move card from Waste to Tableau pile d.
        WF d: Move card from Waste to Foundation pile d.
        SW : Move card from Stock to Waste.
        R: Restart the game (after shuffling)
        H: Display this menu of choices
        Q: Quit the game        
        '''
    option_list = in_str.strip().split()
    
    opt_char = option_list[0][0].upper()
    
    if opt_char in 'RHQ' and len(option_list) == 1:  # correct format
        return [opt_char]
    
    if opt_char == 'S' and len(option_list) == 1:
        if option_list[0].upper() == 'SW':
            return ['SW']
    
    if opt_char == 'W' and len(option_list) == 2:
        if option_list[0].upper() == 'WT' or option_list[0].upper() == 'WF':
            dest = option_list[1] 
            if dest.isdigit():
                dest = int(dest)
                if option_list[0].upper() == 'WT' and (dest < 1 or dest > 7):
                    print("\nError in Destination")
                    return None
                if option_list[0].upper() == 'WF' and (dest < 1 or dest > 4):
                    print("\nError in Destination")
                    return None
                opt_str = option_list[0].strip().upper()
                return [opt_str,dest]
                               
    if opt_char == 'T' and len(option_list) == 3 and option_list[1].isdigit() \
        and option_list[2].isdigit():
        opt_str = option_list[0].strip().upper()
        if opt_str in ['TT','TF']:
            source = int(option_list[1])
            dest = int(option_list[2])
            # check for valid source values
            if opt_str in ['TT','TF'] and (source < 1 or source > 7):
                print("\nError in Source.")
                return None
            #elif opt_str == 'MFT' and (source < 0 or source > 3):
                #print("Error in Source.")
                #return None
            # source values are valid
            # check for valid destination values
            if (opt_str =='TT' and (dest < 1 or dest > 7)) \
                or (opt_str == 'TF' and (dest < 1 or dest > 4)):
                print("\nError in Destination")
                return None
            return [opt_str,source,dest]

    print("\nError in option:", in_str)
    return None   # none of the above


def main():   
    tably,stocky,foundationy, wasty =initialize() # use the function and store it in variables
    print(MENU)# print the menue
    display(tably,stocky,foundationy, wasty)# use display function
    promot = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): ") # promot for an input
    praisy= parse_option(promot)# use the prase function and store it inside a variable
    while 7:# this line would always evaluate true
        if praisy == None:
            display(tably,stocky,foundationy, wasty)# use the display function
            promot = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): ")# promot for an in input
            praisy= parse_option(promot)
            continue
        elif praisy[0].upper() == "TT": # check if the move were TT this condition would evaluate
            if not tableau_to_tableau(tably,praisy[1]-1,praisy[2]-1):
                print("\nInvalid move!\n")
            elif check_win(stocky, wasty,foundationy,tably):# check using the function
                print("You won!")
        elif praisy[0].upper() == "TF":
            if not tableau_to_foundation(tably,foundationy,praisy[1]-1,praisy[2]-1):
                print("\nInvalid move!\n")# print the rror message
            elif check_win(stocky, wasty,foundationy,tably):# use the ceck win functions
                print("You won!")
                break
        elif praisy[0].upper() == "WT":# this line would be evaluated if the user enter "WT"
            if waste_to_tableau(wasty,tably,praisy[1]-1) == False:# if not in tablue
                print("\nInvalid move!\n")# print the error function
            elif check_win(stocky, wasty,foundationy,tably):
                print("You won!")# print the message if it was evaluated True
                break
        elif praisy[0].upper() == "WF":# this would evaluate if the user enter WF
            if not waste_to_foundation(wasty,foundationy,praisy[1]-1):
                print("\nInvalid move!\n")# print error message
            elif check_win(stocky, wasty,foundationy,tably):
                print("You won!")
                break
        elif praisy[0].upper() == "SW":# this would evaluate 
            if not stock_to_waste(stocky,wasty): # check if it is not in waste
                print("\nInvalid move!\n")# the error message that will be printed if it is not in the waste
            elif check_win(stocky, wasty,foundationy,tably):
                print("You won!")  
                break  
        elif praisy[0].upper() == "R": # this choice would be evaluated if the user enter small or capital R
            tably,stocky,foundationy, wasty =initialize()
            print(MENU) # print the menu
        elif praisy[0].upper() == "H": # this choice would be evaluated if the user enter h letter
            print(MENU)  
        elif praisy[0].upper() == "Q":
            break
        display(tably,stocky,foundationy, wasty)# use the display method  in the variables
        promot = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): ")# promot for an input
        praisy= parse_option(promot)           

if __name__ == '__main__':
     main()
