param($ip, $filtro)

Write-Output "Executando ping no host: $ip"

ping -n 3 $ip | Select-String $filtro