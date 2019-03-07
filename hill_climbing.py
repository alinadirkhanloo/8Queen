from QueenAgent import Agent
import numpy as np

board1 = np.array([
    [0, 0, 1, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 3, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 0, 0, 8, 0, 0, 0]]
)
ag = Agent(board1)
print("start")
counter = 0
mc=1
while (mc!=0):
    if counter==64:
        board1=ag.random_board()
        counter=0
        print("****************************************************")
    temp1 = ag.getConflict(board1)
    while counter < 64:
        mc = ag.get_most_conflict()
        board2 = ag.queen_move(mc)
        temp2 = ag.getConflict(board2)
        if temp1 > temp2:
            temp1=temp2
            board1 = board2
            counter += 1
            print(board1)
            print(ag.conflict_list)
            print(temp2)
            print(mc)
            break
        else:
            ag.queen_move(ag.get_most_conflict())
            counter += 1

print("/***************************///////////////////solved//////////////*********")