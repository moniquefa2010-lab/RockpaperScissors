# A simple Rock, Paper, Scissor Game (Without GUI)
# Doesn't give an error when user types abc or Rocker instead of Rock, Paper, Scissor.
# Basically, no error handling (Exception handling is not implemented)

import random  # Imports random module so the computer can randomly choose rock, paper, or scissor

user_action = input('Do you choose rock, paper, or scissor? ')  # Takes user input as a string
possible_action = ['rock', 'paper', 'scissor']  # List of valid choices for the computer
computer_action = random.choice(possible_action)  # random.choice() selects one item randomly from the list
print('You chose ' + user_action + ' and the computer chose ' + computer_action + '.')  # Displays both selections

#Same choice

if user_action.lower() == computer_action:  # lower() converts input to lowercase for case-insensitive comparison
   print('Both players selected ' + user_action + '. It is a tie.')  # If both choices match, it is a tie

#User chooses rock

elif user_action.lower() == 'rock':  # Checks if user selected rock
   if computer_action == 'scissor':  # Rock beats scissor
       print('Rock smashes scissor. You win!')
   else:  # Otherwise computer must have selected paper
       print('Paper covers the rock. The computer wins...')

#User chooses scissor

elif user_action.lower() == 'scissor':  # Checks if user selected scissor
   if computer_action == 'paper':  # Scissor beats paper
       print('Scissor cut paper. You win!')
   else:  # Otherwise computer selected rock
       print('Rock smashes scissor. The computer wins...')

#User chooses paper

elif user_action.lower() == 'paper':  # Checks if user selected paper
   if computer_action == 'rock':  # Paper beats rock
       print('Paper covers rock. You win!')
   else:  # Otherwise computer selected scissor
       print('Scissor cuts paper. The computer wins...')