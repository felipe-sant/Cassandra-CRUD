from src.utils.criarVendedor import criarVendedor

vendedor = criarVendedor(isRequired=True)
if vendedor:
    print(vendedor)
    input()
else:
    print("Operação cancelada")
    input()