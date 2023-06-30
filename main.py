#main file

import os
import time

class GameBoard:
    def __init__(self, gameboard):
        self.gameboard = gameboard
        self.rowLen = len(gameboard)
        self.colLen = len(gameboard[0])

    def __repr__(self):
        res = ""
        rows = len(self.gameboard)
        cols = len(self.gameboard[0])
        for i in range(rows):
            
            if i %3 == 0:
                res += "----------------------------\n"
            for j in range(cols):
                if j%3 == 0:
                    res += " | "
                res += str(self.gameboard[i][j]) + " "
            res += "\n"
        
            
        return res
    
    def update(self, posX, posY, newVal):
        self.gameboard[posX][posY] = newVal
        os.system('cls')
        print(f"\nUpdated position {posX}, {posY} with value : {newVal}")
        print(self)
        
 
    
    def emptyCell(self):
        for posX in range(0, self.rowLen):
            for posY in range(0, self.colLen):
                if self.gameboard[posX][posY] == 0:
                    print(f"\nFound Empty cell at pos {posX},{posY}")
                    return [posX, posY]
                
        return []
                
                
        #if we find no empty cell, we can say we have found the solution
        raise Exception("No empty cells, BOARD IS FULL!")
    

    def isValid(self, posX, posY, value):
        
        #checking row

        if value in self.gameboard[posX]:
            return False
        
        col = []
        for i in range(0, self.colLen):
            col.append(self.gameboard[i][posY])
            

        if value in col:
            return False
        
        #starting point of the block we are in is obtained by these calculations

        block_x = posX // 3
        block_y = posY // 3

        
        posX = block_x * 3
        posY = block_y * 3

        for i in range(posX, posX+3):
            for j in range(posY, posY+3):
                
                if self.gameboard[i][j] == value:
                    
                    return False


        return True




def solveBoard(gb : GameBoard):
    
    pos = gb.emptyCell()
    print("Going deeper...")

    if len(pos) == 0:
        return True
    
    else:

        for i in range(1, 10):

            if gb.isValid(pos[0], pos[1], i):
                gb.update(pos[0], pos[1], i)
                time.sleep(0.05)
                if solveBoard(gb):
                    return True
                
        os.system('cls')
        print("backtracking...") 
        gb.update(pos[0], pos[1], 0)
        
        return False


def run():

    boardData = [
                            [7,8,0,  4,0,0,  1,2,0],
                            [6,0,0,  0,7,5,  0,0,9],
                            [0,0,0,  6,0,1,  0,7,8],

                            [0,0,7,  0,4,0,  2,6,0],
                            [0,0,1,  0,5,0,  9,3,0],
                            [9,0,4,  0,6,0,  0,0,5],

                            [0,7,0,  3,0,0,  0,1,2],
                            [1,2,0,  0,0,7,  4,0,0],
                            [0,4,9,  2,0,6,  0,0,7]
                ]
    
    TestBoardData = [
                            [0,0,0,  0,0,0,  0,0,0],
                            [6,8,0,  0,0,0,  0,0,0],
                            [1,9,0,  0,0,0,  0,0,0],

                            [0,0,0,  0,0,0,  0,0,0],
                            [0,0,0,  0,0,0,  0,0,0],
                            [0,0,0,  0,0,0,  0,0,0],

                            [0,0,0,  0,0,0,  0,0,0],
                            [0,0,0,  0,0,0,  0,0,0],
                            [0,0,0,  0,0,0,  0,0,0],
                ]
    
    gameboard = GameBoard(boardData)

    testBoard = GameBoard(TestBoardData)
    
    print(gameboard)

    solveBoard(gameboard)

    print(gameboard)

    


    
    print('Ended')



run()