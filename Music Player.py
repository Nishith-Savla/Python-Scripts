# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:41:55 2020

@author: Nishith
"""

from pygame import mixer
mixer.init()
mixer.music.load("Lamberghini.mp3")
mixer.music.set_volume(0.5)
mixer.music.play

while True:
    print("Press 'p' to pause")
    print("Press 'r' to resume")
    print("Press 'v' to set volume")
    print("Press 'e' to exit")
    
    ch = input("['p', 'r', 'v', 'e']>>>")
    
    if ch = 'p':
        mixer.music.pause()
    elif ch = 'r':
        mixer.music.unpause()
    elif ch = 'v':
        v = float(input("Enter volume: "))
        mixer.music.set_volume(v)
    elif ch = 'e':
        mixer.music.stop()
        break