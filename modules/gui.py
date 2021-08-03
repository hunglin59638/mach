#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 21:49:22 2021

@author: hunglin
"""

import tkinter as tk
from tkinter import filedialog
from pathlib import Path

def run_gui():
    
    def run_mach_gui():
        from .mach import run_mach
        url = url_entry.get()
        out_dir = dir_entry.get()
        run_mach(url, Path(out_dir))
        
    def explore_dir():
        path = filedialog.askdirectory(initialdir=Path().home())
        dir_path.set(path)
    
    window = tk.Tk()
    window.title("Mach")
    window.geometry('400x300')
    
    header_label = tk.Label(window, text="Donwlond music from Youtube playlist automatically")
    header_label.pack()
    
    url_frame = tk.Frame(window)
    url_frame.pack(side=tk.TOP)
    url_label = tk.Label(url_frame, text="Input playlist url: ")
    url_label.pack(side=tk.LEFT)
    url_entry = tk.Entry(url_frame)
    url_entry.pack(side=tk.LEFT)
    
    dir_frame = tk.Frame(window)
    dir_frame.pack(side=tk.TOP)
    dir_path = tk.StringVar(window)
    dir_entry = tk.Entry(dir_frame, textvariable = dir_path)
    dir_entry.pack(side=tk.LEFT)
    dir_buttom = tk.Button(dir_frame, text="Choose a directory", 
                            command=explore_dir)
    dir_buttom.pack(side=tk.RIGHT)
    
    
    download_buttom = tk.Button(window, text='Download', command=run_mach_gui)
    download_buttom.pack(side=tk.TOP)
    
    window.mainloop()

