
# copy
contatos = {
    "guilherme@gmail.com": {
        "nome": "Guilherme",
        "telefone": "+91123456789"
    },
    "nycolas@gmail.com": {
        "nome": "Nycolas",
        "telefone": "+91123456789"
    },
    "atylas@gmail.com" : {
        "nome": "Atylas",
        "telefone": "+91123456789"
    }
}

copia = contatos.copy()

print(copia)


# fromkeys
pessoa = dict.fromkeys(["nome", "telefone", "idade"], "vazio")

print(pessoa)


# get
print(contatos.get("guilherme@gmail.com"))


# keys
print(contatos.keys())


# values
print(contatos.values())

# pop
print(contatos.pop("guilherme@gmail.om", "não encontrei"))


# popitem
print(contatos.popitem())


# in
resultado = "nycolas@gmail.com" in contatos.keys()
print(resultado)



