import time
import pyautogui
import pyperclip
from PythonMagick import Image

window_name = input("Enter windows title to screenshot: ")
coordinates = tuple(map(int, input("Enter the coordinates for the screenshot: ").split()))
screenshot_filename = input("Enter the filename for the screenshot: ")

window_to_screenshot = pyautogui.getWindowsWithTitle(window_name)[0]
window_to_screenshot.activate()
pyautogui.screenshot('ss.png', coordinates)
Image(screenshot_filename).write("clipboard:")
