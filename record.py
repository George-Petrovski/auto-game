import keyboard
import time

recorded_events = []

def on_key_event(e):
    if e.event_type == keyboard.KEY_DOWN:
        start_time = time.time()
        recorded_events.append((e.name, start_time))
    elif e.event_type == keyboard.KEY_UP:
        end_time = time.time()
        recorded_events[-1] = (recorded_events[-1][0], end_time - recorded_events[-1][1])

keyboard.hook(on_key_event)
keyboard.wait('esc')  # Press 'esc' to stop recording

with open('recorded_events.txt', 'w') as f:
    for event in recorded_events:
        f.write(f"{event[0]} {event[1]}\n")