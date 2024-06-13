param($ip)

if(!$ip){
    Write-Output "Exemplo de uso: .\script.ps1 <ip>"
}else{
    Write-Output "Efetuando ping no host: $ip"
    ping -n 2 $ip | Select-String "bytes=32"
}