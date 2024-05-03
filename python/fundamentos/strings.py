# " " e ' ' indicam string, """ """ indicam string mas com a possibilidade de formatar em blocos.

w = "Nycolas Lasanha"
print(w)

a = """
Esse seria um texto
em blocos."""

print(a)

print(a + w)

# Metodos

#.strip - ignora os espacos antes e depois da string.
print("\nstrip ---")
a = "   Nycolas   "
print(a)
print(a.strip())

#.lower - deixa todas as letras em minusculas.
print("\nlower ---")
a = "NycOlAs"
print(a)
print(a.lower())

#.lower - deixa todas as letras em minusculas.
print("\nupper ---")
a = "NycOlAs"
print(a)
print(a.upper())

#.lower - deixa todas as letras em minusculas.
print("\nfind ---")
a = "NycOlAs"
print(a)
print(a.find("As"))
