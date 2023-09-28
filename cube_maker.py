import pyautogui
import time
import random

# Define the number of iterations you want for the loop
num_iterations = 5
x_coord = 3000
y_coord = 533
print("Starting up cube maker")
# Loop to perform mouse click and move events
for _ in range(num_iterations):
    print("Crafting...")
    pyautogui.moveTo(x=x_coord, y=y_coord, duration=1)
    # Perform a mouse click event
    pyautogui.click()
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(5)
    # Perform a mouse move event (you can specify the coordinates)
    pyautogui.moveTo(x=x_coord-237, y=y_coord-13, duration=1)
    pyautogui.click()
    print("Waiting for timer...")
    # Add a delay if needed
    time.sleep(300)
    # Some extra random amount of time between 1 and 20 seconds of wait
    time.sleep(random.randint(1,20))

print("Finished")