$filter = Read-Host "Filtro para achar o comando PowerShell "
$commands = (Get-Command | Select-String "$filter")

Write-Host "----- Comando esncontrados----- "
$count = 0

# View commands
foreach($command in $commands){
    Write-Host "[$count] - $command"
    $count++
}

#Get Help
$choice = Read-Host "Com qual comando precisa de ajuda"

Get-Help $choice
