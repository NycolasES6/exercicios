param($ip, $porta)

if (!$ip -or !$porta) {
    Write-Host "Scanner do Nycolas"
    Write-Host "Modo de uso: .\script.ps1 <ip> <porta>"
}else{
    if (Test-NetConnection $ip -Port $porta -WarningAction SilentlyContinue -InformationLevel Quiet) {
        Write-Host "Porta $porta ABERTA"
    }else {
        Write-Host "Porta $porta FECHADA"
    }
}
