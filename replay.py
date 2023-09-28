import time
import keyboard

def record_and_playback():
    recorded_data = []

    print("Recording started. Press 'q' to stop recording and 'p' to stop playback.")

    while True:
        keys = keyboard.read_event()
        event_type = keys.event_type
        key = keys.name

        recorded_data.append((event_type, key))

        if key == 'q':
            break
    time.sleep(1000)
    print("Playing back recorded data. Press 'p' to stop playback.")

    for event_type, key in recorded_data:
        if event_type == keyboard.KEY_DOWN:
            keyboard.press(key)
        elif event_type == keyboard.KEY_UP:
            keyboard.release(key)

        if keyboard.is_pressed('p'):
            print("Playback stopped.")
            return

record_and_playback()
