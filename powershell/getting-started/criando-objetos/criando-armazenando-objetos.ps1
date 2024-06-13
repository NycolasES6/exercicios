$newObject = New-Object -TypeName psobject -Property @{
    ComputerName = 'SERVER'
    OS = 'Windows x64'
    Environment = 'Production'
}

Write-Output $newObject

$otherObject = [PSCustomObject]@{
    ComputerName = "SERVER2"
    OS = 'Ubuntu 24.04 LTS'
}

Write-Output $otherObject