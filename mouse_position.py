import pyautogui

# Get the current mouse cursor's position
x, y = pyautogui.position()

print(f"Current mouse cursor position: X={x}, Y={y}")