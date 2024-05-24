# Get-ChildItem | Select-Object Name

# O pipe faz com que o resultado do comando anterior sirva de entrada para o comando seguinte
#Pode ser substituido por

# ""

#gci | Select Name

Get-ChildItem | ForEach-Object{
    Copy-Item -Path $_.FullName -Destination .\new
}