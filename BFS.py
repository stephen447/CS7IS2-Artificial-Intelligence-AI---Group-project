import logic  # File got and modified from , used for game implementation
import util  # File from assignment 1 used for creating the queue for BFS. Unmodified.
import game_func  # Modified file '2048.py' from ... Converted to a function

start_state = mat = logic.start_game()  # Creating initial state of the game
visited = []  # List for the nodes which were visited to prevent them being revisited
visited.append(start_state)  # add the start state to visited nodes
print(len(visited))
fringe = util.Queue()  # The fringe is now a queue for BFS, which operates with FIFO
fr = (start_state, [], 0)  # Start state as matric, empty array for actions, and a zero for current score
fringe.push(fr)  #  Add the start state to the fringe, so its sucessors can be calculated
max_score = 0  # Setting initial maximum score to zero
max_tile = 0

def getSuccessors(matrix, score): #Function for calculating the sucessors and score of a node
    i = 0
    suc = [0, 0, 0, 0]
    actions = ['w', 'a', 's', 'd'] # array with possible actions - up, left, down, right.
    status = logic.get_current_state(mat)  # Get the current state
    if (status == 'GAME NOT OVER'): # if the game isnt over, get successor for all actions
        for act in actions:
            suc[i] = game_func.game(matrix, act, score)  # Read in the state, score and correspond of successor i
            i = i + 1  # Move onto next successor
        return suc  # Return suc with all successor for a state
    else: # else return an empty array if the game is over
        return []


# Main implementation
while not fringe.isEmpty():  #  While the fringe is not empty, keep searching
    cur_node, action, score = fringe.pop()  # Load in next entry in queue to the current node
    successors = getSuccessors(cur_node, score)  # get the sucessors of the current node
    #print(len(visited))
    if successors:
        for suc in successors:  #  for every sucessor of current node
            node = suc[0]  # the node is in position 0 of suc
            if not node in visited:  #  if the node hasnt been visited
                suc_act = suc[1] # get the action for the sucessor from index 1
                suc_score = suc[2] # Get the score of the current node to
                curr_max_tile = suc[3]
                visited.append(node)  # add the node to explored states
                fringe.push((node, action + [suc_act], suc_score))
                #print(curr_max_tile)
                if(curr_max_tile>max_tile):
                  max_tile = curr_max_tile
                if(suc_score>max_score):
                    max_score = suc_score
                    max_action = action + [suc_act]
                    print('New max score: ', max_score)
                    print('Max matrix')
                    print(node[0])
                    print(node[1])
                    print(node[2])
                    print(node[3])
                    print('Max tile of maximum score solution: ', curr_max_tile)
                    print('Global max tile: ', max_tile)
                    print('\n')