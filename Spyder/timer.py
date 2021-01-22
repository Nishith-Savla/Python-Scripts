# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 20:41:28 2020

@author: Nishith
"""


import threading

def tryy():
    print('\nPython.hub\n')
    
timer = threading.Timer(5.0, tryy)

timer.start()
