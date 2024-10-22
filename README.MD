# HID-Script
儲存一些 HID 的 CircuitPython 腳本
## 使用配置
**硬體**: Raspberry Pi Pico W with rp2040

**軟體**: Adafruit CircuitPython 9.1.4

## 安裝HID函式庫
1. 進入 [CircuitPython HID 函式庫](https://github.com/adafruit/Adafruit_CircuitPython_HID)

2. 選擇最新版的 Releases

3. 會看到 `adafruit-circuitpython-hid-8.x-mpy-版本.zip` 或 `adafruit-circuitpython-hid-9.x-mpy-版本.zip`

4. 選擇你自己的 Adafruit CircuitPython 版本(可以至樹梅派的 `boot_out.txt` 查看自己的版本)

5. 下載並解壓縮，將 lib 資料夾的檔案放入自身樹梅派的 lib 資料夾

6. 主要運行的主程式記得命名成 `main\.py` 或 `core\.py`

## 腳本
- Rickroll
    - 打開記事本寫下 "YOU ARE BEEN HACKED" ，並且利用 Powershell 開啟 RickRoll 連結
- Steal_Info
    - 開啟 Powershell ，並且透過 GitHub Raw 功能下載並執行 `Steal_Info_Script.ps1` 的腳本內容(預設是傳送到我的 discord webhook ，可以將專案 fork 後更改 `Steal_Info_Script.ps1` 第一行的 **$webhookUrl** 和 `Steal_Info.py` 的 **RawUrl**)