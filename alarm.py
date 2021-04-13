import datetime
from playsound import playsound

alarmHour = int(input("What hour you want to wake up: "))
alarmMinute = int(input("What minute you want to wake up: "))
amPm = str(input("am or pm: "))

if(amPm == "pm"):
    alarmHour = alarmHour + 12

while True:
    if(alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute):
        print("Wake up")
        playsound('C:\\Users\\Nishith\\Downloads\\alarm.mp3')  # Replace it with the path to your file
        break
