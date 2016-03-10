from tkinter import *
root = Tk()

class Cell (Button):
    Dead = 0
    Live = 1

    def __init__ (self,parent):
        Button.__init__(self,parent, relief = "raised" , width = 2 , borderwidth = 1 , command = self.onpress)
        self.displayState(Cell.Dead)

    def onpress (self):
        if self.state == Cell.Live:
            self.displayState(Cell.Dead)
        elif self.state == Cell.Dead:
            self.displayState(Cell.Live)

    def setNextState (self , Neighbours):
        if self.state == Cell.Live and (Neighbours < 2 or Neighbours > 3):
            self.nextState = Cell.Dead
        elif self.state == Cell.Dead and Neighbours == 3:
            self.nextState = Cell.Live
        elif self.state == Cell.Dead and Neighbours != 3:
            self.nextState = self.state

    def stepToNextState(self):
        self.displayState(self.nextState)

    def displayState (self , newstate):
        self.state = newstate
        if self.state == Cell.Live:
            self["bg"] = "black"
        if self.state == Cell.Dead:
            self["bg"] = "white"

class Grid:
    def __init__(self,parent,sizex,sizey):
        self.sizex = sizex
        self.sizey = sizey
        self.cells = []
        for a in range (0,self.sizex):
            rowcells = []
            for b in range (0, self.sizey):
                c = Cell(parent)
                c.grid(row=b , column=a)
                rowcells.append(c)
            self.cells.append(rowcells)

    def step (self):
        cells = self.cells
        for x in range (0,self.sizex):
            if x==0: x_down = self.sizex-1
            else: x_down = x-1
            if x==self.sizex-1: x_up = 0
            else: x_up = x+1
            for y in range(0,self.sizey):
                if y==0: y_down = self.sizey-1
                else: Y_down = y-1
                if y==self.sizey-1: y_up = 0
                else: y_up = y+1
                sum = cells[x_down][y].state + cells[x_up][y].state + cells[x][y_down].state + cells[x][y_up].state + cells[x_down][y_down].state +cells[x_up][y_up].state + cells[x_down][y_up].state + cells[x_up][y_down].state
                cells[x][y].setNextState(sum)
            for row in cells:
                for cell in row:
                    cell.stepToNextState()

    def clear(self):
        for row in self.cells:
            for cell in row:
                cell.displayState(Cell.Dead)

if __name__ == "__main__":
    frame = Frame(root)
    frame.pack()
    grid = Grid(frame,25,25)
    bottomFrame = Frame(root)
    bottomFrame.pack (side = BOTTOM)
    buttonStep = Button(bottomFrame , text="Step" , command=grid.step)
    buttonStep.pack(side = LEFT)
    buttonClear = Button(bottomFrame, text = "Clear", command=grid.clear)
    buttonClear.pack(side=LEFT , after=buttonStep)
    root.mainloop()