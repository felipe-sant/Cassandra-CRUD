from src.utils.criarVendedor import criarVendedor
from src.utils.criarProduto import criarProduto
from src.utils.limparTerminal import limparTerminal

limparTerminal()
produto = criarProduto(isRequired=True)
if produto:
    print(produto)
    input()
else:
    print("Operação cancelada")
    input()