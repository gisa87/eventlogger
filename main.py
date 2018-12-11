# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 07:53:18 2018

@author: Saverio
"""

from tkinter import Tk, Label, Button

class MyFirstGUI:
    
    def __init__(self,master):
        self.master = master
        master.title("Event logger")
        
        self.label = Label(master, text="prima gui")
        self.label.pack()
        
        self.greet_button = Button(master, text="Log", command=self.saveLog)
        self.greet_button.pack()
        
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
        
    def saveLog():
        print("Test")
            
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()