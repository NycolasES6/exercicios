Write-Host "Hello World with Write-Host"
# Serve somente para STDOUT

Write-Output "Hello World with Write-Output"
# Serve tanto para STDOUT quanto para saida de redirecionamento

$message = Write-Output "Hello World with Write-Output Redirection"

$message


# Write-Output is aliased to Echo or Write

Echo 'Hello world with Echo'
Write "Hello world with Write"

"Hello world "