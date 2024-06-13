param($rede)

if(!$rede){
    Write-Output "Exemplo de uso: .\script 192.168.0"
}else{
    foreach ($ip in 1..254){

        Write-Output "$rede.$ip"
        
        ping -n 1 "$rede.$ip" | Select-String "bytes=32"
    }
}