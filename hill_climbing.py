from QueenAgent import Agent
import time
def start(board):
    bo=board
    counter = 0
    local_optimal=0
    temp1=1
    while (temp1!=0):
        if counter==56:
            bo=ag.random_board()
            counter=0
            local_optimal+=1

        temp1 = ag.getConflict(bo)
        while counter < 56:
            mc = ag.get_most_conflict()
            board2 = ag.queen_move(mc,bo)
            temp2 = ag.getConflict(board2)
            if temp1 > temp2:
                temp1=temp2
                bo = board2
                counter += 1
                break
            else:
                ag.queen_move(ag.get_most_conflict(),board2)
                counter += 1
    return local_optimal

ag = Agent()
avg=0
x=[]
print("start -->")
startime =time.time()
board1=ag.random_board()
for i in range(100):
    x.append(start(board1))
    avg+=start(board1)
    print(i," th solved")
print("--> end")
endtime =time.time()
print(" Average : ",avg/100)
print(" Max Local Optima : ",max(x))
print(" Min Local Optima : ",min(x))
print(" Total Time",endtime-startime)