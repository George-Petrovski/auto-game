import ctypes
import time
import re

SendInput = ctypes.windll.user32.SendInput

W = 0x11
A = 0x1E
S = 0x1F
D = 0x20
Z = 0x2C
UP = 0xC8
DOWN = 0xD0
LEFT = 0xCB
RIGHT = 0xCD
ENTER = 0x1C 

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def pressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def releaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, 
ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

if __name__ == '__main__':
    pressKey(0x11)
    time.sleep(1)
    releaseKey(0x11)
    time.sleep(1)

# Mouse click constants
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

# Function to simulate a mouse click
def clickMouse():
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    
    # Mouse down event
    ii_.mi = MouseInput(0, 0, 0, MOUSEEVENTF_LEFTDOWN, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    # Mouse up event
    ii_.mi = MouseInput(0, 0, 0, MOUSEEVENTF_LEFTUP, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

import pyautogui
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Function to detect the presence of a word in a specified area
def detectWordInArea(top_left_x, top_left_y, width, height):
    # Capture a screenshot of the specified area
    extracted_text = ""
    screenshot = pyautogui.screenshot(region=(top_left_x, top_left_y, width, height))

    # if save_screenshot:
    #     screenshot.save(screenshot_filename)
    #     print(f"Screenshot saved as '{screenshot_filename}'")

    # Perform OCR on the screenshot to extract text
    extracted_text = pytesseract.image_to_string(screenshot, config='--psm 11')

    print(extracted_text)
    print("=========================================================================")
    
    # Check if the target word appears in the extracted text
    str = re.findall("STR.*%", extracted_text)
    print(str)
    if len(str) > 1 and "6" in ''.join(str):
        print("Crazy STR potential found")
        return True
    
    dex = re.findall("DEX.*%", extracted_text)
    print(dex)
    if len(dex) > 1 and "6" in ''.join(dex):
        print("Crazy DEX potential found")
        return True
    
    int = re.findall("INT.*%", extracted_text)
    print(int)
    if len(int) > 1 and "6" in ''.join(int):
        print("Crazy INT potential found")
        return True
    
    luk = re.findall("LUK.*%", extracted_text)
    print(luk)
    if len(luk) > 1 and "6" in ''.join(luk):
        print("Crazy LUK potential found")
        return True
    
    return False


area_top_left_x = 601  # Define the top-left corner X coordinate of the area
area_top_left_y = 456  # Define the top-left corner Y coordinate of the area
area_width = 170       # Define the width of the area
area_height = 47      # Define the height of the area

result = detectWordInArea(area_top_left_x, area_top_left_y, area_width, area_height)

print("pre-check")

if result:
    print("Good Potential")
else:
    print("Not good Potential")

print("Staring in")
for i in reversed(range(5)):
    print(i)
    time.sleep(1)


count = 0
while(detectWordInArea(area_top_left_x, area_top_left_y, area_width, area_height) == False):
    count += 1
    clickMouse()
    time.sleep(1)
    pressKey(ENTER)
    time.sleep(0.15)
    pressKey(ENTER)
    time.sleep(0.15)
    pressKey(ENTER)
    time.sleep(0.15)
    pressKey(ENTER)
    time.sleep(2)

print("Optimal Epic is reached using cubes: ", count)