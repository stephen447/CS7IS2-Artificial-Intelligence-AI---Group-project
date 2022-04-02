import logic  # This is the logic function for the game_func
import numpy as np  # Numpy library
import random, game_func_q # importing random library and game_func

class QLearningAgent:
    def __init__(self):
        self.Q = {}  # Dictionary with the q value for corresponsing states and actions
        self.epsilon = 0.1  # epsilon parameter for deciding random actions
        self.alpha = 0.1  # Alpha is for weighting the new q values relative to old one
        self.discount = 0.95  # Discount for rewards

    def learn(self): # Main implementation of RL
        # Initialise game
        state = logic.start_game() # Get the start state
        print(state)
        current_score = 0  # The score is zero for start state

        while True: #while the game hasnt reached a terminal state
            game_status = logic.get_current_state(state)  # Get the current status of the game
            if(game_status == 'WON'):  # If the game_status is WON, the episode is over and it should break
                break
            elif(game_status == 'LOSS'):  # If the game_status is LOSS, the episode is over and it should break
                break
            else:  # Otherwise the game isnt over and must continue to learn q values
                actions = self.getLegalActions(state)  # Get the actions of the current state
                for act in actions:  # For every action
                    game = game_func_q.game(state, act, current_score) # Run the game to get the successor, reward,
                    next_state = game[0]  # The successor for given action
                    reward = game[3]  # The reward for the given action - essentially the rewards is the improvement in the score by action taken
                    #max_q_next_state = self.computeValueFromQValues(next_state)  # Get the max q value of the next state
                    self.update(state, act, next_state, reward)  # Update the current value of the action in question
                chosen_action = self.getAction(state)  # Get the action for the updated q values
                game = game_func_q.game(state, chosen_action, current_score)  # Run the game for the chosen action in order to update the state for the next run
                state = game[0]  # Update current state
                current_score = game[1]  # Update the current state

    def getLegalActions(self, state):

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

    def getQValue(self, state, action):
        # This function checks the q dictionary to see if we have visited this state before, it returns 0 if it hasnt or returns the q value if it has
        if (state, action) not in self.Q:
            return 0.0
        return self.Q[(state, action)]

    def computeValueFromQValues(self, state):
        # This returns the max q value for a given state
        actions = self.getLegalActions(self, state)
        if not actions:
            return 0
        return max([self.getQValue(state, a) for a in actions])

    def computeActionFromQValues(self, state):
        # This function returns the best action for a state by finding max q value
        # If there is multiple actions with same q value it will return a random choice between them
        actions = self.getLegalActions(state)
        if not actions:
            return None
        best_q_value = self.computeValueFromQValues(state)
        best_actions = [a for a in actions if self.getQValue(state, a) == best_q_value]
        return random.choice(best_actions)

    def getAction(self, state):
        # This function return the action to take by returning a ranom action epsilon proportion of the time, otherwise it returns the optimal action
        legalActions = self.getLegalActions(state)
        p = self.epsilon
        if not legalActions:
            return None
        greedy_flag = random.random()
        if greedy_flag < self.epsilon:
            return random.choice(legalActions)
        else:
            return self.computeActionFromQValues(state)

    def update(self, state, action, nextState, reward):
        # This function update the q value for a given state, action pair
        alpha = self.alpha  # Alpha value
        print(nextState)
        sample = reward + self.discount * self.computeValueFromQValues(nextState)  # New q value
        self.Q[state, action] = (1 - alpha) * self.getQValue(state, action) + alpha * sample # q value for a given state and action is the old value and new value merged


def __main__():
    agent = QLearningAgent()
    for i in range(100):
        mean_max_tile = 0
        for _ in range(20):
            agent.learn()
            #mT = agent.game_field.maxTile()
            #print(mT, agent.weights)
            #mean_max_tile += mT
        print(mean_max_tile / 20)
        print(len(agent.Q))
        # print(agent.Q)




__main__()