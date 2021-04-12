import sys
from time import sleep
import pyautogui


def switch_to_browser():
    window = pyautogui.getWindowsWithTitle("Udemy")[-1]
    if window:
        window.activate()
    else:
        sys.exit(-1)


def confirm_enroll(timeout=30):
    seconds_waited = 0
    while seconds_waited < timeout:
        enroll_btn2 = pyautogui.locateCenterOnScreen(
            "udemyEnrollerImages/udemy-enrollnow2.png", grayscale=True, confidence=0.9)
        print(f"enroll_btn2: {enroll_btn2}")
        if enroll_btn2:
            pyautogui.click(enroll_btn2)
            break
        else:
            sleep(2)
            seconds_waited += 2


def enroll_in_course():
    enroll_btn1 = pyautogui.locateCenterOnScreen(
        "udemyEnrollerImages/udemy-enrollnow.png", grayscale=True, confidence=0.9)
    start_button = pyautogui.locateCenterOnScreen(
        "udemyEnrollerImages/udemy-startcourse.png", grayscale=True, confidence=0.8)
    goto_button = pyautogui.locateCenterOnScreen(
        "udemyEnrollerImages/udemy-gotocourse.png", grayscale=True, confidence=0.9)
    print(f"enroll_btn1: {enroll_btn1}")
    if enroll_btn1:
        pyautogui.click(enroll_btn1)
    elif start_button or goto_button:
        pyautogui.hotkey('ctrl', 'w')
        return
    confirm_enroll()


def enrollAll(count):
    for i in range(count):
        print(pyautogui.getActiveWindowTitle())
        if "Udemy" not in pyautogui.getActiveWindowTitle():
            pyautogui.hotkey('ctrl', 'tab')
        enroll_in_course()


switch_to_browser()
# enroll_in_course()
enrollAll(6)
