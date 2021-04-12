# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 21:02:17 2020

@author: Nishith
"""

import qrcode

url = input("Enter the url to make QR code: ")
img = qrcode.make(url)
img.save('qrimage.png')

print('Done👍')
