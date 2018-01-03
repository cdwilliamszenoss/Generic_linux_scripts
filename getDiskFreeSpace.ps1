$disks = Get-WmiObject -Query "Select * from Win32_LogicalDisk"
$driveName = "C:"
$driveID = "Test"

foreach($disk in $disks)
    { 
      If ($disk.Name -eq $driveName ) {
      
        '{"values": {"": {"'+ $driveID + '":' + $disk.FreeSpace + '}}, "events": []}'
      }
    }
