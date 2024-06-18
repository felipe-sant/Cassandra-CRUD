from src.utils.limparTerminal import limparTerminal
from src.utils.formatarTexto import formatarTexto_negrito
from src.functions.adicionarProduto import adicionarProduto
from src.functions.listarProduto import listarProduto
from src.functions.removerProduto import removerProduto
from src.classes.vendedor import Vendedor
from src.classes.compra import Compra

def menuCampoProdutos(colecao: Compra | Vendedor) -> Compra | Vendedor:
    while True:
        limparTerminal()
        
        print("--" * 21)
        print(formatarTexto_negrito("Menu Campo Produtos"))
        print("1 - Adicionar Produto")
        print("2 - Listar Produtos Atuais")
        print("3 - Listar Produtos Totais")
        print("4 - Remover Produto")
        print("0 - Concluir")
        print("--" * 21)
        
        opcao = input("\nDigite a opção desejada: ")
        
        match opcao:
            case "1":
                colecao = adicionarProduto(colecao)
            case "2":
                listarProduto(colecao.produtos)
            case "3":
                listarProduto()
            case "4":
                colecao = removerProduto(colecao)
            case "0":
                return colecao
            case _:
                print("Opção inválida")
                input()

# Path: src/layouts/menuCampoProdutos.py