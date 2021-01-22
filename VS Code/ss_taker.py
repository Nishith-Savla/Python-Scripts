import time
import pyautogui
import pyperclip
from PIL import Image
# from jaraco import clipboard
from PythonMagick import Image

brave_window = pyautogui.getWindowsWithTitle('vlabs')[0]
vscode_window = pyautogui.getWindowsWithTitle('vlabs')[0]
brave_window.activate()
time.sleep(1)
pyautogui.screenshot('ss.png', [43, 25, 1053, 704])
Image("ss.png").write("clipboard:")
