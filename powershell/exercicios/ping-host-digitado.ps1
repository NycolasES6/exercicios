$ip = Read-Host "Digite o ip da busca: "

Write-Output "Executando Ping no host $ip"

ping -n 7 $ip | Select-String "bytes=32"