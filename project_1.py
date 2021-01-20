# This is a rock paper sissors game with implemented methods

# importing a random method for the computer to use
import random

# Print message opening the users to the game
print('Welcome to the ROCK PAPER SISSORS CHAMPIONSHIP!!!! \n'
+ 'Since you\'ve made it this far im sure you know the rules but just in case you\'ve just been lucky ill go over them again \n' 
+ 'ROCK BEATS SISSORS \n'
+ 'PAPER BEATS ROCK \n'
+ 'SISSORS BEATS PAPER \n')


def main():

    # Gets the Computers input
    computer_input = random.randint(1, 3)

    # This will turn the computers input into a string using the same validator i send the users input to
    computer_input = r_p_s_1_2_3(computer_input)

    # asks the user what they want to pick
    user_input = int(input('Please select Rock, Paper, or Sissors: \n'
    + '1 = Rock, 2 = Paper, 3 = Sissors \n'))

    #send the user input to a validator
    user_input = validation_input(user_input)

    #send the user and the computers input to a method seeing if it won loss or tied
    win_loss_tie = w_l_t(user_input, computer_input)

    #print message letting the user know what they picked and suspense for what the CPU will pick
    print(f'Good choice on {user_input} Now lets see what the computer picked \n'
    + '.........................................\n'
    + '.........................................\n'
    + '.........................................\n'
    + f'{computer_input}\n'
    +f'{win_loss_tie}')

    # see if the user wants to play again
    again = input('Would you like to play again? y or n ')
    if again == 'y' or again == 'Y':
        main()
    elif again == 'n' or again == 'N':
        print('Have a good day hope to see you in the championship again soon!')
    else:
        print('Please enter y or n ')         



    



# do all the possibilitys of outcomes, then send the outcome to another method to ask the user if they want to try again
def w_l_t(human_choice, computer_choice):
    if human_choice == 'ROCK' and computer_choice == 'ROCK':
        return 'TIE'
    elif human_choice == 'ROCK' and computer_choice == 'PAPER':
        return 'LOSS :('
    elif human_choice == 'ROCK' and computer_choice == 'SISSORS':
        return 'YOU WIN!!!! CONGRATULATIONS ON WINNING THE CHAMPIONSHIP! NOW GO CELEBRATE'
    elif human_choice == 'PAPER' and computer_choice == 'ROCK':
        return 'YOU WIN!!!!! CONGRATULATIONS ON WINNING THE CHAMPIONSHIP'
    elif human_choice == 'PAPER' and computer_choice == 'PAPER':
        return 'TIE'
    elif human_choice == 'PAPER' and computer_choice == 'SISSORS':
        return 'LOSS :('
    elif human_choice == 'SISSORS' and computer_choice == 'ROCK':
        return 'LOSS :('
    elif human_choice == 'SISSORS' and computer_choice == 'PAPER':
        return 'YOU WIN!!!!!! CONGRATULATIONS ON WINNING THE CHAMPIONSHIP!!! NOW GO CELEBRATE'
    elif human_choice == 'SISSORS' and computer_choice == 'SISSORS':
        return 'TIE'
    else:
        print('Sorry there was an error we usually try to get these cleaned up for the championship but we make mistakes')


                        



    


# validate that the input the user made was correct and then send it to a different method to return a string 
def validation_input(choice):
    while choice > 3 or choice < 1:
        choice = int(input('Please enter 1 for Rock, 2 for Paper, or 3 for Sissors: \n'))
    choice = r_p_s_1_2_3(choice)
    return choice


def r_p_s_1_2_3(num):
    if num == 1:
        return 'ROCK'
    elif num == 2:
        return 'PAPER'
    elif num == 3:
        return 'SISSORS'                         
       




main()