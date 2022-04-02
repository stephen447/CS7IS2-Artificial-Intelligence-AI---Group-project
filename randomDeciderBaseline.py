# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 17:52:08 2022

@author: store
"""

import logic  # This is the logic function for the game_func
import numpy as np  # Numpy library
import random, game_func_q # importing random library and game_func
import matplotlib.pyplot as plt
import random


def getLegalActions(state):
    legal_actions = []  # List with successors, sucessor scores, actions
    actions = ['w', 'a', 's', 'd']  # array with possible actions - up, left, down, right.
    status = logic.get_current_state(state)  # Get the current state
    if (status == 'GAME NOT OVER'):  # if the game isnt over, get successor for all actions
        for act in actions:
            successor = game_func_q.game(state, act, 0)  # Read in the state, score and correspond of successor i
            suc_mat = successor[0]  # the sucessor is stored in position 0 of sucessor list
            if suc_mat != state:  # if the sucessor isnt the same as the current state - otherwise it will get stuck in infinite loop
                legal_actions.append(act)  # add sucessor to list of sucessors to be returned

        return legal_actions  # Return suc with all successors for a state
    else:  # else return an empty array if the game is over and no sucessors for given node
        return []


def guess():  # Main implementation of random
    # Initialise game
    state = logic.start_game()  # Get the start state
    current_score = 0  # The score is zero for start state

    while True: #while the game hasnt reached a terminal state
        game_status = logic.get_current_state(state)  # Get the current status of the game
        print(game_status)
        if game_status == 'WON':  # If the game_status is WON, the episode is over and it should break
            print('Game Won')
            break
        elif game_status == 'LOST':  # If the game_status is LOSS, the episode is over and it should break
            print('Game Lost')
            break
        else:  # Otherwise the game isnt over and must continue to learn q values
            actions = getLegalActions(state)  # Get the actions of the current state
            if (len(actions)>0):
                # for act in actions:  # For every action
                #     game = game_func_q.game(state, act, current_score) # Run the game to get the successor, reward,
                #     next_state = game[0]  # The successor for given action
                #     reward = game[3]  # The reward for the given action - essentially the rewards is the improvement in the score by action taken
                #     update(state, act, next_state, reward)  # Update the current value of the action in question
                randomIndex = random.randrange(0, len(actions) - 1)
                chosen_action = actions[randomIndex]  # Get the action for the updated q values
                game = game_func_q.game(state, chosen_action, current_score)  # Run the game for the chosen action in order to update the state for the next run
                state = game[0]  # Update current state
                max_tile = game[3]  # Update the max tile
                current_score = game[2]  # Update the current state

    return state, current_score, max_tile  # returning the max tile and score


highestScorePerEpisode = []
highestTilePerEpisode = []

def plotPerformancePerEpisode(highestScore, highestTile):
    plt.figure()
    plt.rc('font', size=18)
    plt.rcParams['figure.constrained_layout.use'] = True
    plt.plot(range(1,50), highestScore, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12, label = 'Highest score')  #Highest score in green -> 50 episodes
    plt.plot(range(1,50), highestTile, color='red', marker='x', linestyle='dashed', linewidth=2, markersize=12, label = 'Highest tile')  #Highest tile in red -> 50 episodes
    plt.title('Performance of random agent over 50 episodes')
    plt.show()



def __main__():
    global_max_tile = 0  # Initialising the global max tile
    global_max_score = 0  # Initialising the global
    episodes = 50  # No. of episode to run for the algorithm - tune this
    print('here')
    for _ in range(episodes):
        guesserResult = guess()
        state = guesserResult[0]  # State achieved
        current_score = guesserResult[1]  # Reading in the current score achieved for current episode
        current_max_tile = guesserResult[2]
        highestScorePerEpisode.append(current_score)
        highestTilePerEpisode.append(current_max_tile)

        if current_max_tile > global_max_tile:  # Checking if latest episode achieved new global max
            global_max_tile = current_max_tile
            max_tile_state = state
            print('New global max tile : ', global_max_tile)
            print('Max tile state', max_tile_state)

        if current_score > global_max_score:  # Checking if latest episode achieved new global max
            global_max_score = current_score
            max_score_state = state
            print('New global max tile : ', global_max_tile)
            print('Max score state', max_score_state)
        

    print('Max score achieved: ', global_max_score)  # Printing the max score achieved over all episodes
    print('Max score state:')
    print(max_score_state[0])
    print(max_score_state[1])
    print(max_score_state[2])
    print(max_score_state[3])

    print('Max tile achieved: ', global_max_tile)  # Printing the max tile achieved over all episodes
    print('Max tile state:')
    print(max_tile_state[0])
    print(max_tile_state[1])
    print(max_tile_state[2])
    print(max_tile_state[3])

    plotPerformancePerEpisode(highestScorePerEpisode, highestTilePerEpisode)    

__main__()  # Call main function to run code
