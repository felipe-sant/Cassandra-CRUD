from src.utils.criarVendedor import criarVendedor
from src.utils.criarProduto import criarProduto
from src.utils.limparTerminal import limparTerminal
from src.utils.criarCompra import criarCompra

limparTerminal()
compra = criarCompra(isRequired=True)
if compra:
    print(compra)
else:
    print("Compra não criada")
