'''
Created on 27-Nov-2019

@author: sneha
'''
import random
import string
import copy

class GridGame():
    
    
    colorArray = string.ascii_uppercase


    def __init__(self, orig=None, size=10, color=4):
        #initializing array params for grid and other temp variables

        self.colorArray = self.colorArray[0:color]  
        self.size = size
        self.grid = [[' ' for i in range(self.size)] for i in range(self.size)]
        self.FC = 0
        self.gridFilled = []
        self.colorGroups = []
        self.reset()

        if orig:
            self.colorArray = copy.deepcopy(orig.colorArray)
            self.size = orig.size
            self.grid = copy.deepcopy([list(col) for col in orig.grid])
            self.FC = copy.deepcopy(orig.FC)
            self.gridFilled = copy.deepcopy(orig.gridFilled)
            self.colorGroups = copy.deepcopy(orig.colorGroups)


    def fillGrid(self):

        while True:
            done = True
            for coor in self.gridFilled:
                
                x, y = coor
                for n, g in enumerate(self.colorGroups):
                    if self.FC == g[0]:
                        if (y < self.size and (x, y + 1) in g[1]) or (x <= self.size and (x + 1, y) in g[1]):
                            tempg = g[1] 
                            done = False
                            break
                if not done:
                    break
            if done:
                break
            else:
                self.gridFilled += tempg  
                del self.colorGroups[n]
    
    def printGrid(self):
        print()
        for i in range(self.size):
            print (self.grid[i])
        print()

    def move(self, c):
        self.FC = c
        for coor in self.gridFilled:
            x, y = coor
            self.grid[x][y] = c
        self.fillGrid()


    def children(self):
        children = []
        for c in self.colorArray:
            if c != self.FC:
                child = GridGame(orig=self)
                child.move(c)
                if len(child.colorGroups) < len(self.colorGroups):
                    children.append((child, c))
        return children


    def findNextTileColor(self,b):
        children = list(sorted(self.children(), key=lambda x: x[0].score()))
        return children[0][1]

    def isOver(self):
        if len(self.colorGroups) == 0:
            return True
        else:
            return False
    def score(self):
        return len(self.colorGroups)

    def scoree(self):
        return len(self.gridFilled)
    def reset(self):
        # reset the color array with the changing tile color
        for i in range(self.size):
            for j in range(self.size):
                temp = self.colorArray[random.randrange(len(self.colorArray))]
                self.grid[i][j] = temp
                self.colorGroups.append([temp, [(i, j)]])

        while True:
            done = True
            for n, g in enumerate(self.colorGroups):
                for coor in g[1]:
                    x, y = coor
                    for m, gg in enumerate(self.colorGroups):
                        if n != m and g[0] == gg[0]:
                            if (y > 0 and (x, y - 1) in gg[1]) or (x > 0 and (x - 1, y) in gg[1]):
                                if n < m:
                                    tempg = g
                                    tempg[1] = tempg[1] + gg[1]
                                    keep = n
                                    dele = gg
                                if n > m:
                                    tempg = gg
                                    tempg[1] = tempg[1] + g[1]
                                    keep = m
                                    dele = g
                                done = False
                                break
                    if not done:
                        break
                if not done:
                    break
            if done:
                break
            else:
                self.colorGroups[keep] = tempg
                self.colorGroups.remove(dele)

        self.FC = self.colorGroups[0][0]
        self.gridFilled = self.colorGroups[0][1]
        del self.colorGroups[0]
        

class FindPath(GridGame):
    def __init__(self, board):
        super().__init__()
        self.open = [(board, "")]
        self.board = board

    def findNextTileColor2(self):

        x = 0
        tileSequence=[]
        while len(self.open) > 0:
            
            x+=1
            b, move = self.open[0]
            tileSequence.append(move)
            if b.isOver():
                print("path ",move)
                return move

            children = b.children()
            for child, m in children:
                self.open.append((child, move+m))

            del self.open[0]


# def getUserMovesAndColors1(n,m,b):
#     tileColorSequence = []             
#     moves = 0
#     while not b.isOver():
#         moves += 1
#         tileColor = b.findNextTileColor(b)
#         print("Chosen Tile Color ", tileColor)
#         tileColorSequence.append(tileColor)
#         b.move(tileColor)
#         b.printGrid()
#     print("Number of moves made ", moves)
#     print("Sequence of colors chosen by user", tileColorSequence)
#     
#     return moves,tileColorSequence
    

def getUserMovesAndColors(n,m,b):
    moves = 0
    p = FindPath(b)
    path=p.findNextTileColor2()
    for move in path:
        moves+=1
        b.move(move)
        b.printGrid()
    print("Number of moves made ", moves)
    print("Sequence of colors chosen by user", path)
    return moves,path

if __name__ == '__main__':
    
    N = int(input("size of grid n :"))
    M = int(input("no of colors in grid m :"))
    b = GridGame(size=N, color=M) 
    a=b
    #method 1
    #getUserMovesAndColors1(N,M,b)
    
    #method 2
    getUserMovesAndColors(N,M,a)
    
    

    
    
    
