import pyautogui
import time

def replay_event(key, duration):
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)

with open('recorded_events.txt', 'r') as f:
    for line in f:
        key, duration = line.split()
        replay_event(key, float(duration))