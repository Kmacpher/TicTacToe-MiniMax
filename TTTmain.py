# Tic-Tac-Toe (in Python)
# Written by Karen MacPherson, 9/18/05
# Uses modified code written for the book Artificial Intelligence: A Modern Approach

import Karengames
#imports the players, search algorithms, and TicTacToe(game) class

def main():
    "Main function of TTTmain.py. Defines the game parameters and starts game. Loops until user does not play again."
    printIntructions()
    a = 'y'
    while (a=='y'):
        num_players, diff, first = get_player_info()
        k, h = get_game_info()
        #print "\n\nSTART GAME!\n\n"
        g = Karengames.TicTacToe(k, h)
        play_game_diff(g, num_players, diff, first)
        a = raw_input("\nWould you like to play again? (y/n): ").lower()
    
    
def get_player_info():
    "Queries for user input for number of players, difficulty, and if the player wants to go first"
    while (True):
        num = raw_input("Please enter the number of players (0, 1, 2): \n")
        if num.isdigit() and int(num) < 3:
            num_players = int(num)
            break
        else:
            print "Invalid Input. "
    if num_players==0 or num_players == 1:
        while (True):
            d = raw_input("Enter 1 for hard difficulty and 0 for easy difficulty: \n").strip()
            if d.isdigit() and (int(d)==0 or int(d)==1):
                diff = int(d)
                break
            else:
                print "Invalid Input. "
    else:
        diff = 0
    if num_players == 1:
        while (True):
            f = raw_input("Do you want to go first? (y/n): ").lower()
            if f=='y':
                first = 1
                break
            if f=='n':
                first = 0
                break
            else:
                print "\nInvalid Input. "
    else:
        first = 0
 
    return num_players, diff, first
        
   
    
def get_game_info():
    "Queries the user for h, the height of the board, and k, the number of symbols in a line needed for a win."
    #k cannot be larger than h.
    #hxh dimensions, right now is sqaure.
    #defalt is h=3, k=3. An invalid input will return the defaults
    
    h = raw_input("\nEnter the height and width of the sqaure board:").strip()
    if (not h.isdigit()) or int(h)<=0:
        print "\nInvalid Input. The height and width will be 3.\n"
        h = 3
    else:
        h = int(h)
    k = raw_input("\nHow many in a row make a victory?: ").strip()
    if (not k.isdigit()) or int(k)<=0 or int(k)>h:
        print "\nInvalid Input. You will need {0} in a row to win.\n".format(h)
        k = h
    else:
        k = int(k)
    return h, k
    
def printIntructions():
    "Prints the instructions to the screen."
    print "\n\n**** Welcome to Tic-Tac-Toe ****"
    print 
    print "You make a move by typing a number 1-x on"
    print "the keyboard. The numbers correspond to a"
    print "position on the board, where x is the number"
    print "of positions on the board."
    print "A player wins when they align a given"
    print "number of X's or O's before the other player.\n\n"
    


def play_game_diff(g, num_players, diff, first):
    "Determines what arguments to use for play_game based on the user's input. Calls play_game."
    if num_players==0:
        if diff:
            #print "ab vs ab"
            Karengames.play_game(g, Karengames.alphabeta_player, Karengames.alphabeta_player)
        else:
            #print "r vs r"
            Karengames.play_game(g, Karengames.random_player, Karengames.random_player)
    elif num_players==1:
        if diff:
            if first:
                #print "qu vs ab"
                Karengames.play_game(g, Karengames.query_player, Karengames.alphabeta_player)
            else:
                #print "ab vs qu"
                Karengames.play_game(g, Karengames.alphabeta_player, Karengames.query_player)
        else:
            if first:
                #print "qu vs r"
                Karengames.play_game(g, Karengames.query_player, Karengames.random_player)
            else:
                #print "r vs qu"
                Karengames.play_game(g, Karengames.random_player, Karengames.query_player)
    else:
        #print "qu vs qu"
        Karengames.play_game(g, Karengames.query_player, Karengames.query_player)
      
            
if __name__ == "__main__":
    main()