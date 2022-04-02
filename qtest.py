import logic  # This is the logic function for the game_func
import numpy as np  # Numpy library
import random, game_func_q # importing random library and game_func

Q = {}  # Dictionary with the q value for corresponsing states and actions
epsilon = 0.1  # epsilon parameter for deciding random actions
alpha = 0.1  # Alpha is for weighting the new q values relative to old one
discount = 0.95  # Discount for rewards

def tup(matrix):  # Used to convert the state from a list to a tuple - lists cant be stored in dictionary
    result = [tuple(l) for l in matrix]
    return tuple(result)


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

def getQValue(state, action):
        # This function checks the q dictionary to see if we have visited this state before, it returns 0 if it hasnt or returns the q value if it has
        state = tup(state)
        if (state, action) not in Q:
            return 0.0
        return Q[(state, action)]

def computeValueFromQValues(state):
    # This returns the max q value for a given state
    actions = getLegalActions(state)
    if not actions:
        return 0
    return max([getQValue(state, a) for a in actions])

def update(state, action, nextState, reward):
    # This function update the q value for a given state, action pair

    print(nextState)
    sample = reward + discount * computeValueFromQValues(nextState)  # New q value
    state = tup(state)
    Q[state, action] = (1 - alpha) * getQValue(state, action) + alpha * sample # q value for a given state and action is the old value and new value merged


def computeActionFromQValues(state):
    # This function returns the best action for a state by finding max q value
    # If there is multiple actions with same q value it will return a random choice between them
    actions = getLegalActions(state)
    print('actions are', actions)
    if len(actions) < 1:
        return None
    else:
        best_q_value = computeValueFromQValues(state)
        best_actions = [a for a in actions if getQValue(state, a) == best_q_value]
        print('best actions are', best_actions)
        return random.choice(best_actions)


def getAction(state):
    # This function return the action to take by returning a ranom action epsilon proportion of the time, otherwise it returns the optimal action
    legalActions = getLegalActions(state)
    p = epsilon
    if not legalActions:
        return None
    greedy_flag = random.random()
    if greedy_flag < epsilon:
        return random.choice(legalActions)
    else:
        return computeActionFromQValues(state)


def learn():  # Main implementation of RL
    # Initialise game
    state = logic.start_game()  # Get the start state
    print(state)
    current_score = 0  # The score is zero for start state

    while True: #while the game hasnt reached a terminal state
        game_status = logic.get_current_state(state)  # Get the current status of the game
        if game_status == 'WON':  # If the game_status is WON, the episode is over and it should break
            print('Game Won')
            break
        elif game_status == 'LOST':  # If the game_status is LOSS, the episode is over and it should break
            print('Game Lost')
            break
        else:  # Otherwise the game isnt over and must continue to learn q values
            actions = getLegalActions(state)  # Get the actions of the current state
            if (len(actions)>0):
                for act in actions:  # For every action
                    game = game_func_q.game(state, act, current_score) # Run the game to get the successor, reward,
                    next_state = game[0]  # The successor for given action
                    reward = game[3]  # The reward for the given action - essentially the rewards is the improvement in the score by action taken
                    update(state, act, next_state, reward)  # Update the current value of the action in question
                chosen_action = getAction(state)  # Get the action for the updated q values
                game = game_func_q.game(state, chosen_action, current_score)  # Run the game for the chosen action in order to update the state for the next run
                state = game[0]  # Update current state
                current_score = game[2]  # Update the current state
                print(current_score)




def __main__():
    for i in range(100):
        mean_max_tile = 0
        for _ in range(20):
            learn()
        print(mean_max_tile / 20)

__main__()