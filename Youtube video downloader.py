# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 21:21:15 2020

@author: Nishith
"""

import pytube
url = "https://www.youtube.com/watch?v=3ociATLe100"

video = pytube.YouTube(url)
youtube = video.streams.first
youtube.download(r'C:/Users/Nishith/Downloads')
