"""
-------------------------------------------------------
 Simulates a Rock, Paper, Scissors game,
 allowing the user to play against the computer with 
 randomized choices and providing the outcome of each round.
-------------------------------------------------------
Author:  Ramina Manouchehri
ID:      169042249
Email:   mano2249@mylaurier.ca
__updated__ = "2023-11-14"
-------------------------------------------------------
"""
# Imports
import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    print("My choice was: ", computer)
    
    if user == computer:
        return 'It\'s a tie'
    
        # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())
