import random
import tkinter as tk
from functools import partial
import time


class memcards(tk.Frame):
  def __init__(self, parent, items):
    super().__init__(parent)
    self.parent = parent
    self.grid()

    self.flipped = set()
    self.current = []
    self.memorder = [None for i in range(len(items)*2)]
    self.dictionary = items
    self.keys = list(items.keys())
    self.values = list(items.values())
    self.shuffle()
    self.definemap()
    self.createlabel()

  def createlabel(self):
    self.label = tk.Label(self, text = "The Rows and Columns start at 0, not 1; #"
    + " means unflipped; _ means correct")
    self.label.grid(row = len(self.memorder)//len(self.currmap[0]), column = 0, rowspan = 2, 
    columnspan = len(self.currmap[0]), sticky = tk.W+tk.S)
    self.label.config(bg = "purple")

  def definemap(self):
    # figure out potential heights and widths
    divisors = []
    for i in range(len(self.memorder)):
      if (len(self.memorder))%(i+1) == 0:
        divisors.append(i+1)
    # gets the real width and height of map
    width = divisors[len(divisors)//2]
    height = divisors[(len(divisors)//2)-1]
    themap = [[None for i in range(width)] for x in range(height)]
    for x in range(height):
      for i in range(width):
        themap[x][i] = tk.Button(self, text = "#", command = partial(self.flip, x, i))
        themap[x][i].grid(row = x, column = i, ipadx = 10, ipady = 5)
        themap[x][i].config(bg = 'light blue')
    self.currmap = themap

  def shuffle(self):
    doneitems = {}
    while len(self.memorder) >len(doneitems):
      itemloc = random.randint(0,len(self.keys)-1)
      b = random.randint(0,1)
      memorderloc = random.randint(0,len(self.keys*2)-1)
      if memorderloc not in doneitems.values():
        if b == 0 and self.memorder[memorderloc] not in self.keys:
          self.memorder[memorderloc] = self.keys[itemloc]
          doneitems[self.memorder[memorderloc]] = memorderloc
        if b == 1 and self.memorder[memorderloc] not in self.values:
          self.memorder[memorderloc] = self.values[itemloc]
          doneitems[self.memorder[memorderloc]] = memorderloc

  def flip(self, row, column):
    self.currmap[row][column]['text'] = self.memorder[
        (row * len(self.currmap[0])) + column]
    self.currmap[row][column].grid(row = row, column = column)
    self.current.append([self.memorder[(row * len(self.currmap[0])) + column],[row, column]])

  def unflip(self, correct: bool):
    if correct:
      self.flipped.add(self.current[0][0])
      self.flipped.add(self.current[1][0])
      self.currmap[self.current[0][1][0]][self.current[0][1][1]]['text'] = "__"
      self.currmap[self.current[1][1][0]][self.current[1][1][1]]['text'] = "__"
      self.label['text'] = "Correct"
    else:
      self.currmap[self.current[0][1][0]][self.current[0][1][1]]['text'] = "#"
      self.currmap[self.current[1][1][0]][self.current[1][1][1]]['text'] = "#"
      self.label['text'] = "Incorrect"
    self.current = []

  def mainloop(self):
    try:
      while 1:
        self.update_idletasks()
        self.update()
        if len(self.current) == 2:
          if self.current[0][0] in self.dictionary and self.dictionary[self.current[0][0]] == self.current[1][0]:
            time.sleep(0.5)
            self.unflip(True)
          elif self.current[1][0] in self.dictionary and self.dictionary[self.current[1][0]] == self.current[0][0]:
            time.sleep(0.5)
            self.unflip(True)
          else: 
            time.sleep(0.5)
            self.unflip(False)
        if len(self.flipped) == len(self.memorder):
          self.label['text'] = "Congratulations, you win!"
        time.sleep(0.01)
    except: pass




items = {'a': 1, 'b':2, 'c':3, 'd': 4}


root = tk.Tk()
root.minsize(150, 100)
app = memcards(root, items)
app.mainloop()
