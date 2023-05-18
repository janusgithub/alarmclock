#python code

from datetime import datetime
import time
import pygame

def set_alarm():
    hour = int(input("Enter the hour (24-hour format): "))
    minute = int(input("Enter the minute: "))
    return hour, minute

def check_alarm(alarm_hour, alarm_minute):
    while True:
        now = datetime.now()
        if now.hour == alarm_hour and now.minute == alarm_minute:
            print("Wake up!")
            pygame.mixer.init()
            pygame.mixer.music.load(r"C:\Users\jahna\Downloads\The_Weeknd_Starboy_(NaijaMusic.NG).mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue
            break
        time.sleep(60)

alarm_hour, alarm_minute = set_alarm()
check_alarm(alarm_hour, alarm_minute)
