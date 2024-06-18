param($ip)

$popularPorts = 21, 22, 23, 80, 443, 3306

if(!$ip){
    Write-Host "----- Modo de uso -----"
    Write-Host ".\script [host]"
    Write-Host "-----------------------"
}else{
    foreach ($port in $popularPorts){
        if(Test-NetConnection $ip -Port $port -WarningAction SilentlyContinue -InformationLevel Quiet){
            Write-Host "$port : Aberta"
        }
    }
}