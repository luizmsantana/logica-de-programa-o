cadastros = [
    "  joao da silva;11988887777  ",
    "  maria sousa;21977776666  ",
    "  carlos edgardo oliveira;31966665555  ",
    "  ana paula lima;41955554444  "
]

print("==================================================")
print("       SISTEMA DE TRATAMENTO DE CADASTROS")
print("==================================================\n")

for cadastro_bruto in cadastros:
    registro = cadastro_bruto.strip()
    partes = registro.split(";")

    nome = partes[0].upper()
    telefone = partes[1]
    ddd = telefone[:2]

    print(f"Funcionário: {nome} | DDD: {ddd} | Telefone: {telefone}")

print("\n==================================================")
print("             TRATAMENTO FINALIZADO")
print("==================================================")