import random

def play():
    user = input("Make a choice: 'r' for rock, 'p' for paper, 's' for scissors ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie!'
        
    return is_winner(user, computer)

    # r > s, s > p, p > r

def is_winner(player, opponent):
    if (player == 'r' and opponent == 's'):
        return 'You win!!'
    elif (player == 's' and opponent == 'p'):
        return 'You win!!'
    elif (player == 'p' and opponent == 'r'):
        return 'You win!!'
    else:
        return 'Computer wins.'


print(play())