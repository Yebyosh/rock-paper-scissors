# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random

our_play = ""

# second param is opt; used only if wanna keep track of oppo hist
# input is string of R, P, S (oppo prev move) - 1st game empty
# output also string (next move) R, P, or S
def player(prev_play, opponent_history=[], our_history=[]):
    # doubt use of NN (since lessons taught about training and no supplied databases)
    # going to go with intent of demonstrating ML understanding
    # go with a play based on history of opponent moves and tweak settings to achieve goal
    if prev_play == '':
        opponent_history.clear()
        our_history.clear()
    else:
        opponent_history.append(prev_play)

    global our_play
    winning_move = {'P': 'S', 'R': 'P', 'S': 'R'}
    losing_move = {'P': 'R', 'R': 'S', 'S': 'P'}

    if prev_play == '':
        our_play = random.choice(['R', 'P', 'S'])
    elif len(opponent_history) < 25:
        if winning_move[prev_play] == our_play:
            our_play = winning_move[our_play]
        elif losing_move[prev_play] == our_play:
            our_play = winning_move[prev_play]
        else:
            our_play = random.choice(['R', 'P', 'S'])
    else:
        srch_trm = opponent_history[-4:]
        ln = len(srch_trm)

        for idx in range(len(opponent_history) - ln):
            if srch_trm == opponent_history[idx: idx + ln]:
                #print(f'Found at {idx}')
                our_play = winning_move[opponent_history[idx + ln]]
                break
            else:
                our_play = random.choice(['R', 'P', 'S'])


    our_history.append(our_play)

    #if len(opponent_history) > 995:
    #    print(f'Our history: {len(our_history)}')

    return our_play

# DA INTERNET
# if you lose the first round, switch to the thing that beats the thing your opponent just played. If you win, don't keep playing the same thing, but instead switch to the thing that would beat the thing that you just played
# When you're at a loss of what to do, throw paper. Because scissors is the least thrown move, statistically, and because rock is the most thrown move, paper is the safest way to go.
    #global our_play

    #print(f'Oppo played: {prev_play}')

    #if prev_play == '':
    #    our_play = random.choice(['R', 'P', 'S'])
    #else:
    #    winning_move = {'P': 'S', 'R': 'P', 'S': 'R'}
    #    losing_move = {'P': 'R', 'R': 'S', 'S': 'P'}

    #    if winning_move[prev_play] == our_play:
    #        our_play = winning_move[our_play]
    #    elif losing_move[prev_play] == our_play:
    #        our_play = winning_move[prev_play]
    #    else:
    #        our_play = random.choice(['R', 'P', 'S'])

    #print(f'We played: {our_play}')

    #return our_play;

# ORIGINAL
    #guess = "R"
    #if len(opponent_history) > 2:
    #    guess = opponent_history[-2]

    #return guess

# test with play
# play(player1, player2, num_games[, verbose])
# players = quincy mrugesh kris abbey human random_player
# main launces to play with 1st 4; each 1000 times
# uncomment main.py last line to auto-run test_module
