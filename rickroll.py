# 作用:
# 縮小所有視窗，開啟記事本並打上"YOU ARE BEEN HACKED"
# 然後透過powershell開啟rickroll連結(可能會有卡輸入法的問題)

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

time.sleep(5)

kbd.press(Keycode.WINDOWS)
time.sleep(0.1)
kbd.send(Keycode.D)
time.sleep(0.1)
kbd.release(Keycode.WINDOWS)
time.sleep(0.5)

open("notepad")

kbd.press(Keycode.CONTROL)
time.sleep(0.1)
kbd.send(Keycode.A)
time.sleep(0.1)
kbd.release(Keycode.CONTROL)
time.sleep(0.3)
kbd.send(Keycode.BACKSPACE)
time.sleep(0.5)

kbd.press(Keycode.CONTROL)
time.sleep(0.3)
mouse.move(0, 0, 20) 
time.sleep(0.2)
kbd.release(Keycode.CONTROL)
time.sleep(0.3)
layout.write("YOU ARE BEEN HACKED", delay = 0.1)
time.sleep(0.5)
kbd.press(Keycode.ALT)
time.sleep(0.1)
kbd.send(Keycode.SHIFT)
time.sleep(0.1)
kbd.release(Keycode.ALT)
time.sleep(0.5)
open("powershell")
time.sleep(1)
kbd.send(Keycode.SHIFT)
time.sleep(0.5)
layout.write('Start-Process "https://www.youtube.com/watch?v=dQw4w9WgXcQ"', delay = 0.1)
kbd.send(Keycode.ENTER)