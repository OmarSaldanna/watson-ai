# import the main function
from modules.ai import AI
# library to detect keybaord
from pynput import keyboard
# others ...
import time
import sys
import os

# variables to check the state of the keys
command_pressed = False
option_pressed = False
last_detection_time = 0
COOLDOWN_SECONDS = int(os.environ["COOLDOWN"])

# start the AI with the current file
ai = AI(sys.argv[1])

# function when a key is pressed
def on_press(key):
    # define global variables
    global command_pressed, option_pressed, last_detection_time
    # try to detect
    try:
        # get the current time
        current_time = time.time()
        # if keys are pressed
        if key in [keyboard.Key.cmd_l, keyboard.Key.cmd_r]:
            command_pressed = True
        elif key in [keyboard.Key.alt_l, keyboard.Key.alt_r]:
            option_pressed = True
        # if both
        if command_pressed and option_pressed:
            # detect the cooldown
            if current_time - last_detection_time >= COOLDOWN_SECONDS:
                print(f">>> Shortcut detected")
                # use AI then
                ai()
                # set the variable to new events
                last_detection_time = current_time
    # if there were an error just skip
    except AttributeError:
        pass


# when a key is released
def on_release(key):
    # global variables
    global command_pressed, option_pressed
    # just set the variables as false
    if key in [keyboard.Key.cmd_l, keyboard.Key.cmd_r]:
        command_pressed = False
    elif key in [keyboard.Key.alt_l, keyboard.Key.alt_r]:
        option_pressed = False


# start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()