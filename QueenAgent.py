import random
import numpy as np

class Agent(object):
    def __init__(self):
        self.board = 0
        self.conflict = 0
        self.conflict_list={1:[0,0,0],2:[0,0,0],3:[0,0,0],4:[0,0,0],5:[0,0,0],6:[0,0,0],7:[0,0,0],8:[0,0,0]}

    def getConflict(self,board):
        self.conflict = 0
        self.conflict_list = {1: [0, 0, 0], 2: [0, 0, 0], 3: [0, 0, 0], 4: [0, 0, 0], 5: [0, 0, 0], 6: [0, 0, 0],
                              7: [0, 0, 0], 8: [0, 0, 0]}
        self.board=board
        for m, i in enumerate(self.board):
            for n, j in enumerate(i):
                if j:
                    cc=0
                    k=m
                    f=n
                    while f<7 :
                        f += 1
                        if self.board[k][f]:
                           cc+=1
                    f = n
                    while f>0 :
                        f -= 1
                        if self.board[k][f]:
                           cc+=1
                    k = m
                    f = n
                    while k < 7:
                        k += 1
                        if self.board[k][f]:
                            cc += 1
                    k = m
                    while k > 0:
                        k -= 1
                        if self.board[k][f]:
                            cc += 1
                    k=m
                    f=n
                    while f<7 and k<7:
                        f += 1
                        k += 1
                        if self.board[k][f]:
                           cc+=1

                    k = m
                    f = n
                    while f>0 and k<7:
                        f -= 1
                        k += 1
                        if self.board[k][f]:
                           cc+=1
                    k = m
                    f = n
                    while f < 7 and k >0:
                        k-=1
                        f+=1
                        if self.board[k ][f]:
                            cc += 1
                    k = m
                    f = n
                    while f > 0 and k >0:
                        k-=1
                        f-=1
                        if self.board[k ][f ]:
                            cc += 1
                    # temp=self.conflict_list[j]
                    self.conflict_list[j]=[cc,m,n]
                    self.conflict+=cc
        return self.conflict

    def get_most_conflict(self):
        for key, value in self.conflict_list.items():
            if value == max(self.conflict_list.values()):
                return key
                break
        return None

    def queen_move(self,m,board):
        self.board=board
        i=self.conflict_list[m]
        self.board[i[1]][i[2]]=0
        while True:
            j = random.randrange(8)
            if j!=i[2]:
                self.board[i[1]][j]=m
                break
        return  np.array(self.board)

    def random_board(self):
        c=[]
        self.board = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]
        )
        for i in range(1,9):
            m=i-1
            n=random.randrange(8)
            while n in c:
                n = random.randrange(8)
            self.board[m][n]=i
            c.append(n)
        return self.board
















