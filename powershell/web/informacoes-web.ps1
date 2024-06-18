$site = Read-Host "Digite o site para informações "

$web = Invoke-WebRequest -Uri $site -Method Options

Write-Host "O servidor roda: "
$web.headers.server
Write-Host ""

Write-Host "O servidor aceita os métodos: "
$web.headers.allow
Write-Host ""

Write-Host "----- Links encontrados -----"
$web2 = Invoke-WebRequest -Uri $site
$web2.Links.Href | Select-String http://
Write-Host "----- Links encontrados -----"