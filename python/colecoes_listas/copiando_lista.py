times = ["Chicago Bulls", "Miami Heat", "Lakers", "Utah Jazz"]

# Se copiarmos com o operador de atribuição eles terão a mesma
# referência, então se modificarmos uma lista, também modificamos a 
# outra.

times2 = times

print("\nSem a modificação --- ---")
print(times)
print(times2)

print("\nCom modificação --- ---")
times.append("Maverycks")
print(times)
print(times2)

# Dessa forma, criamos um novo endereço na memória, assim um não vai 
# modificar caso o outro mude.
print("\nlista = lista2.copy() --- ---")
times = times2.copy()
times.append("Boston Celtics")
print(times)
print(times2)
