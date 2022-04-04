# 2048.py

# importing the logic.py file
# where we have written all the
# logic functions used.
import logic  # Modified this to
import numpy as np

def game(current_matrix, x, curr_score):
    # we have to move up
    if (x == 'W' or x == 'w'):

        # call the move_up function
        mat, flag, score = logic.move_up(current_matrix)
        logic.add_new_2(mat)

    # to move down
    elif (x == 'S' or x == 's'):

        # call the move_down function
        mat, flag, score = logic.move_down(current_matrix)
        logic.add_new_2(mat)


    # to move left
    elif (x == 'A' or x == 'a'):

        # call the move_left function
        mat, flag, score = logic.move_left(current_matrix)
        logic.add_new_2(mat)

    # to move right
    elif (x == 'D' or x == 'd'):

        # call the move_right function
        mat, flag, score = logic.move_right(current_matrix)
        logic.add_new_2(mat)

    else:
        print("Invalid Key Pressed")

    # Creating rewad for terminal states - win and loss
    curr_state = logic.get_current_state(mat)
    if(curr_state == 'WON'):  # Reward of 4096 for win state
        state_val = 500000
    elif(curr_state == 'LOST'):  # Reward of -4096 for lost state
        state_val = -500000
    else:  # Value of zero for game not over state - just leave the reward as the score for these states
        state_val = 0

    reward = score+state_val  # Reward - is the score improvement from the last state to the next. I also weight the terminal states of win and loss appropriately
    new_score = curr_score + score  # calculating new score
    max_tile = np.max(mat)  # return max tile of current state

    # print the matrix after each move.
    # print(mat[0])
    # print(mat[1])
    # print(mat[2])
    # print(mat[3])
    # print('\n')

    return mat, x, new_score, max_tile, reward  # return new matrix, action, new score, max tile of current node


