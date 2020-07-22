# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:15:11 2020

@author: Akatsuki Team
"""
import pandas as pd
import eyed3
import glob
import wx
from tkinter.filedialog import askopenfilenames
import pandas as pd
import glob

root = tk.Tk() 
root.geometry('200x150') 

def open_file():
    global filenames
    filenames = askopenfilenames(title = "Open CSV files") 
    li = []
    for filename in filenames:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)
        frame = pd.concat(li, axis=0, ignore_index=True)
        frame.to_csv('compiled.csv')
def save():
    global filenames
    files = [('All Files', '*.*'),('CSV Files', '*.csv*')]
    filenames = asksaveasfile(filetypes = files, defaultextension = files)
    
btn = Button(root, text ='Open', command = lambda:open_file()) 
btn.pack(side = TOP, pady = 10) 

btn = ttk.Button(root, text = 'Save', command = lambda : save()) 
btn.pack(side = TOP, pady = 20) 

mainloop() 
