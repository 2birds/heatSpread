#!/usr/bin/python
class Board(object):
    """Represents all the cells of a square game-of-life board"""
    def __init__(self, side):
        self.side=side
        self.cells={}
        self.nextCells={}
        for x in range(self.side):
            for y in range(self.side):
                self.cells[(x,y)]=0

    def __str__(self):
        b=''
        for i in self.cells:
            if self.cells[i] == 100:
                alive="very hot"
            else:
                alive="very cold"
            b+="Cell "+str(i)+" is "+alive+".\n"
        return b

    def switchState(self, cell, temp="hot"):
        """Sets the heat state of a give cell(x,y)"""
        if temp == "hot":
            if self.cells[cell] < 100:
                self.cells[cell] = 100
            else:
                self.cells[cell] = 0
        elif temp == "cold":
            if self.cells[cell] > -1:
                self.cells[cell] = -1
            else:
                self.cells[cell]=0

    def nextState(self, cell):
        """Determines and stores the next state of a given cell (x, y)"""
        offTheMap=0
        #print "Moving state.."
        warmth=0
        for x in [-1, 1]:
            for y in [-1, 1]:
                try:
                    cellTemp=self.cells[((cell[0]+x),(cell[1]+y))]
                    if cellTemp != -1:
                        warmth += cellTemp
                    #print warmth
                except:
                    offTheMap+=1
        if self.cells[cell] == 100:
            self.nextCells[cell] = 100
        elif self.cells[cell] == -1:
            self.nextCells[cell] = -1
        else:
            self.nextCells[cell]=warmth/4            

        #print "State moved."

    def step(self):
        """Thin method for advancing the state of the board one step"""
        for cell in self.cells:
            self.nextCells[cell]=0 # Wipes nextCells clean.
            self.nextState(cell)
        for nc in self.nextCells:
            self.cells[nc]=self.nextCells[nc]
        
                            
