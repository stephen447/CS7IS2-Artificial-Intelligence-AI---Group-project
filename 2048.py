# 2048.py

# importing the logic.py file
# where we have written all the
# logic functions used.
import logic
global actual_score

# Driver code
if __name__ == '__main__':
    # calling start_game function
    # to initialize the matrix
    mat = logic.start_game()
    actual_score = 0

while (True):

    # taking the user input
    # for next step
    x = input("Press the command : ")

    # we have to move up
    if (x == 'W' or x == 'w'):

        # call the move_up function
        mat, flag, score = logic.move_up(mat)

        # get the current state and print it
        status = logic.get_current_state(mat)
        print(status)

        # if game not ove then continue
        # and add a new two
        if (status == 'GAME NOT OVER'):
            logic.add_new_2(mat)

        # else break the loop
        else:
            break

    # the above process will be followed
    # in case of each type of move
    # below

    # to move down
    elif (x == 'S' or x == 's'):
        mat, flag, score = logic.move_down(mat)
        status = logic.get_current_state(mat)
        print(status)
        if (status == 'GAME NOT OVER'):
            logic.add_new_2(mat)
        else:
            break

    # to move left
    elif (x == 'A' or x == 'a'):
        mat, flag, score = logic.move_left(mat)
        status = logic.get_current_state(mat)
        print(status)
        if (status == 'GAME NOT OVER'):
            logic.add_new_2(mat)
        else:
            break

    # to move right
    elif (x == 'D' or x == 'd'):
        mat, flag, score = logic.move_right(mat)
        status = logic.get_current_state(mat)
        print(status)
        if (status == 'GAME NOT OVER'):
            logic.add_new_2(mat)
        else:
            break
    else:
        print("Invalid Key Pressed")

    # print the matrix after each
    # move.
    actual_score = actual_score+score
    print('actual_score', actual_score)

    print(mat[0])
    print(mat[1])
    print(mat[2])
    print(mat[3])


