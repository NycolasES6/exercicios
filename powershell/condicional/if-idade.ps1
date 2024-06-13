$idade = Read-Host "Quantos anos você tem: "

if ($idade -ge "18"){
    Write-Output "Com $idade anos, você pode dirigir."
}else{
    Write-Output "Com $idade anos, você não pode dirigir"
}