
import random, util, logic, game_func
class qlearning(ReinforcementAgent): # Reinforcement agent needs to be defined

    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)

        "*** YOUR CODE HERE ***"
        self.values = util.Counter()  #  Initialising dictionary for q values with a defualt value of zero for every state

    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        "*** YOUR CODE HERE ***"
        q_value = self.values[(state, action)]  #  Calculates the q value of a given action in a aiven state

        return q_value

    def getLegalActions(state):
        legal_actions = []  # List with successors, sucessor scores, actions
        actions = ['w', 'a', 's', 'd']  # array with possible actions - up, left, down, right.
        status = logic.get_current_state(state)  # Get the current state
        if (status == 'GAME NOT OVER'):  # if the game isnt over, get successor for all actions
            for act in actions:
                successor = game_func.game(state, act, 0)  # Read in the state, score and correspond of successor i
                suc_mat = successor[0]  # the sucessor is stored in position 0 of sucessor list
                if suc_mat != state:  # if the sucessor isnt the same as the current state - otherwise it will get stuck in infinite loop
                    legal_actions.append(act)  # add sucessor to list of sucessors to be returned
            return legal_actions  # Return suc with all successors for a state

        else:  # else return an empty array if the game is over and no sucessors for given node
            return []

    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        "*** YOUR CODE HERE ***"

        actions = self.getLegalActions(state)  # Getting available actions
        q_value = float("-infinity")  #  let q value be - infinity initially
        if len(actions) == 0:  # If there is no actions, return 0 - terminal state
            return 0

        else:
            for current_action in actions:  # cycling through every action
                current_value = self.getQValue(state, current_action)  #  getting the q value for the actions
                if current_value > q_value:  #  if the current q value is greater than the max, set that as the new max
                    q_value = current_value
        return q_value  #  return the max q value

    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        "*** YOUR CODE HERE ***"
        best_actions = []  #  Array for the action(s) with max q value
        possible_actions = self.getLegalActions(state)  # get the legal actions from the state
        max_q = self.computeValueFromQValues(state)  # Max q value for state in question

        if len(possible_actions) == 0:  #  If there is no legal actions, return 0 - terminal state
            return None

        else:
            for action in possible_actions:
                if self.getQValue(state,
                                  action) == max_q:  # If current action q value is equal to the max q value - its the best action
                    best_actions.append(action)  # Add the action to list of best actions
            act = random.choice(best_actions)  # If there is multiple best actions, pick a random one

        return act  # return the action
        # util.raiseNotDefined()

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.

          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        # Pick Action
        possible_actions = self.getLegalActions(state)
        action = None
        "*** YOUR CODE HERE ***"
        if util.flipCoin(self.epsilon) == True:  # Flipping coin which will be true for epsilon amount of time
            action = random.choice(
                possible_actions)  #  choose random action epsilon amount of times - explor new actions to cover search space
        else:  # Other wise use q value to determine action by calling function
            action = self.computeActionFromQValues(state)
        return action  #  return the action determined

        def update(self, state, action, nextState, reward):
            """
              The parent class calls this to observe a
              state = action => nextState and reward transition.
              You should do your Q-Value update here

              NOTE: You should never call this function,
              it will be called on your behalf
            """
            "*** YOUR CODE HERE ***"
            current_state = self.getQValue(state, action)  #  update q value of current state
            next_state = self.computeValueFromQValues(nextState)  #  update q value of next state

            self.values[(state, action)] = current_state + self.alpha * (
                        reward + self.discount * (next_state) - current_state)  # Bellman equation

            def getPolicy(self, state):
                return self.computeActionFromQValues(state)

            def getValue(self, state):
                return self.computeValueFromQValues(state)




