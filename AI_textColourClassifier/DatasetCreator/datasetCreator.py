from tkinter import *
import csv, random

class appColourPicker(Frame):  

    def __init__(self, master=None):
        Frame.__init__(self, master)
        
        self.dataset = []
        self.colours = []
        self.colour = '#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.colours.append(self.colour)
        self.btnHeight = 20
        self.btnWidth = 50
        
        self.pack()
        self.createWidgets()

    def update(self) :
        self.colour = '#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if self.colour in self.colours :
            print('same colour')
            self.update()
        else :
            self.blackBtn["bg"] = self.colour
            self.whiteBtn["bg"] = self.colour
            self.colours.append(self.colour)

    def black (self, colour) :
        self.dataset.append([colour, 0])
        self.update()

    def white(self, colour):
        self.dataset.append([colour, 1])
        self.update()

    def collection(self) : #Function to convert all data into a csv file for easier use later on when training a neural net.
        cpDataset = open("cpDataset.csv", "w", newline="")
        writer = csv.writer(cpDataset)
        writer.writerows(self.dataset)
        cpDataset.close()

    def createWidgets(self):
        self.blackBtn = Button(self, fg = "black", bg = self.colour, height = self.btnHeight, width = self.btnWidth)
        self.blackBtn["text"] = "Black Text"
        self.blackBtn["command"] = lambda: self.black(self.colour)
        self.blackBtn.pack({'side' : "left"})

        self.whiteBtn = Button(self, fg = "white", bg = self.colour, height = self.btnHeight, width = self.btnWidth)
        self.whiteBtn["text"] = "White Text"
        self.whiteBtn["command"] = lambda: self.white(self.colour)
        self.whiteBtn.pack({"side" : "left"})

        self.complete = Button(self, height = self.btnHeight)
        self.complete["text"] = "Collection completed?"
        self.complete["command"] =  self.collection

        self.complete.pack({"side":"left", "fill": "x"})

        self.QUIT = Button(self, height = self.btnHeight)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "bottom", "fill": "x"})

root = Tk()
root.title("ColourPicker Dataset Creator")
app = appColourPicker(master=root)
app.mainloop()
root.destroy()

