tupla = ("item1", "item2", "item3", "item4")
dicio = dict.fromkeys(tupla, "Nycolas")
dicio["item1"] = "Nycolas"

print(dicio)

print("\n --- ---")
pessoa = {
    "Nycolas":{
        'idade':23,
        'endereco':{
            'rua':'Rua marajoara',
            'casa':12,
            'UF':'DF'
        }
    },
    "Atylas":{
        'idade':19,
        'endereco':{
            'rua':'Rua do Sol',
            'casa':23,
            'UF':'GO'
        }
    },
    "Eryck":{
        'idade':34,
        'endereco':{
            'rua':'Rua da Lua',
            'casa':45,
            'UF':'SC'
        }
    }
}

print(pessoa)
