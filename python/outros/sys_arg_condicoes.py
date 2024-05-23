import sys

print(len(sys.argv))

print(sys.argv[0])

if len(sys.argv) <= 2:
    print("""Iforme no mínimo dois parâmetros.
                <script> ip porta""")
else:
    print("Varrendo o host:", sys.argv[1], "na porta", sys.argv[2])
