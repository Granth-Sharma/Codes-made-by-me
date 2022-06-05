I haven't programmed it but for just the sake of information's avalibility to me I am putting it here.




#!/usr/bin/python3.8


# Prerequisites:
# python 3.8+
# pynput 1.6.7+
# pip3 install pynput
# or for same version when the file was created
# pip3 install pynput==1.6.7

import random
import time

from pynput import keyboard, mouse
from pynput.keyboard import Key
from pynput.mouse import Button, Controller

mouse = Controller()


def key_check(key):
    """Checks what combination of keys has been pressed and acts upon it"""
    # Set var to global
    global looping_1sec_hit
    global looping_mouse_scroll
    global looping_mouse_down_left
    global feeding
    global feed_delay

    try:
        # Set flag for feeding
        if key in COMBINATION_feeding:
            current_pressed_keys.add(key)
            if all(k in current_pressed_keys for k in COMBINATION_feeding):
                if feeding == 1:
                    feeding = 0
                    print('\nNot using the off hand')
                else:
                    feeding = 1
                    feed_delay = 20
                    print('\nOff hand delay is 20 seconds')

        if key in COMBINATION_feeding_increase:
            current_pressed_keys.add(key)
            if all(k in current_pressed_keys for k in COMBINATION_feeding_increase):
                if feed_delay < 30:
                    feed_delay =+ feed_delay + 2
                    print('\nIncreased by 2 seconds to', feed_delay)
                else:
                    print('\nYou have reached the maximun time limit of 30 seconds')

        if key in COMBINATION_feeding_decrease:
            current_pressed_keys.add(key)
            if all(k in current_pressed_keys for k in COMBINATION_feeding_decrease):
                if feed_delay > 2:
                    feed_delay =+ feed_delay - 2
                    if feed_delay < 2:
                        feed_delay = 2
                    print('\nDecreased by 2 seconds to', feed_delay)
                else:
                    print('\nYou have reached the minimum time of 2 seconds')

        # 1 second left mouse press and release.
        if key in COMBINATION_looping_1sec_hit:
            current_pressed_keys.add(key)
            if all(k in current_pressed_keys for k in COMBINATION_looping_1sec_hit):
                print('\nLeft mouse button pressed and released every 1 second')
                looping_1sec_hit = True

        # Mouse wheel scrolling
        if key in COMBINATION_looping_mouse_scroll:
            current_pressed_keys.add(key)
            if all(k in current_pressed_keys for k in COMBINATION_looping_mouse_scroll):
                print('\nScrolling mouse wheel for random section on hotbar')
                looping_mouse_scroll = True

        if key in COMBINATION_hold_down_mouse_left:
            current_pressed_keys.add(key)
            if all(k in current_pressed_keys for k in COMBINATION_hold_down_mouse_left):
                print('\nLeft mouse been held down')
                looping_mouse_down_left = True

        # Exit condition
        if key in COMBINATION_stop_action:
            current_pressed_keys.add(key)
            if all(k in current_pressed_keys for k in COMBINATION_stop_action):
                print('\nStopping and reseting all options.')
                looping_1sec_hit = False
                looping_mouse_scroll = False
                looping_mouse_down_left = False
                mouse.release(Button.left)
                mouse.release(Button.right)
                feeding = 0
                start_program_intro()
        else:
            pass

    except AttributeError:
        print('\nKey check error')


def on_release(key):
    """Tracks when a key has been released"""
    try:
        current_pressed_keys.remove(key)
    except KeyError:
        pass


def scroll_wheel():
    """Scrolls the mouse wheel at a rate of 1 to 9 steps in the veritacl position"""
    random_spin = random.randrange(1, 10)
    mouse.scroll(dx=0, dy=random_spin)


def mouse_press_release_left():
    """Presses and releases the left mouse button"""
    mouse.press(Button.left)
    mouse.release(Button.left)


def mouse_press_release_right():
    """Presses and releases the left mouse button"""
    mouse.press(Button.right)
    mouse.release(Button.right)


def feed():
    """Checks to see if enought time has passed before using the right mouse button for a set time"""
    global beginTime
    global feeding
    global feed_delay
    # print('Checking if feeding is set to True')
    if feeding == 1 and (time.time() - beginTime) >= feed_delay:
        print('\nUsing off hand')
        mouse.release(Button.right)
        mouse.release(Button.left)
        mouse.press(Button.right)
        time.sleep(2)
        mouse.release(Button.right)
        beginTime = time.time()
    else:
        pass

# Program intro and holding before starting
def start_program_intro():
    """Shows a print of the commands that can be used"""
    print('''
AFK Minecraft

Current commands are 
1 second hit with left mouse
    <alt_l> + y

Scroll the mouse wheel for random Hotbar section.
    <alt_L> + u
    
Constant left mouse button
    <alt_l> + i
    
Use off hand every set amount of seconds. Default is 20 seconds between use.
Can be toggled on and off to rest. 
    Toggle on and off
    <alt_l> + j
    
    Increase time
    <alt_l> + h
    
    Decrease time
    <alt_l> + g
    
Stop actions
Will reset all options back to default, including feeding.
    <alt_l> + <Backspace>

<ctrl> + c in the terminal window to end program or close the window.

''')
    input('Press Enter to continue...')

    print('waiting for key input...')

# Setting up the key combination
# The key combination to check
COMBINATION_looping_1sec_hit = {keyboard.Key.alt_l, keyboard.KeyCode.from_char('y')}		# left clicking every second
COMBINATION_looping_mouse_scroll = {keyboard.Key.alt_l, keyboard.KeyCode.from_char('u')}	# scrolling the mouse wheel
COMBINATION_hold_down_mouse_left = {keyboard.Key.alt_l, keyboard.KeyCode.from_char('i')}	# holding down the left mouse buttom
COMBINATION_feeding = {keyboard.Key.alt_l, keyboard.KeyCode.from_char('j')}					# turn on the feeding option
COMBINATION_feeding_increase = {keyboard.Key.alt_l, keyboard.KeyCode.from_char('h')}        # increase delay
COMBINATION_feeding_decrease = {keyboard.Key.alt_l, keyboard.KeyCode.from_char('g')}        # decrease delay
COMBINATION_stop_action = {keyboard.Key.alt_l, Key.backspace}	                            # cancel all actions

# The currently active modifiers recording the current keys been pressed
current_pressed_keys = set()

# sets the initial state of the global references
looping_1sec_hit = False
looping_mouse_scroll = False
looping_mouse_down_left = False
feeding = 0
feed_delay = 20

# Run at the start
start_program_intro()

# Set up for listener
listener = keyboard.Listener(
    on_press=key_check,
    on_release=on_release
)
listener.start()

while True:
    # print('main loop')
    # print(feeding)
    time.sleep(1)
    beginTime = time.time()
    while looping_1sec_hit:
        print('\nLoop 1 second left mouse press and release')
        mouse_press_release_left()
        time.sleep(1)
        feed()
    while looping_mouse_scroll:
        print('\nMouse scroll Hotbar')
        scroll_wheel()
        time.sleep(0.1)
        feed()
    while looping_mouse_down_left:
        mouse.press(Button.left)
        print('\nLeft mouse pressed')
        feed()




