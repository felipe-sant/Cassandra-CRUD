from src.utils.limparTerminal import limparTerminal
from src.functions.listarProduto import listarProduto
from src.utils.formatarTexto import formatarTexto_negrito

def menuAdicionarProduto(colecao = None, isVendedor = False):
    if colecao is None:
        limparTerminal()
        id = input("Digite o ID da coleção: ")
    
    while True:
        limparTerminal()
        
        print("--" * 21)
        print(formatarTexto_negrito("Menu Adicionar Produto"))
        print("1 - Adicionar Produto")
        print("2 - Listar Produtos da coleção")
        print("3 - Listar Produtos Cadastrados")
        print("4 - Remover Produto")
        print("0 - Concluir")
        print("--" * 21)
        
        opcao = input("\nDigite a opção desejada: ")
        
        match opcao:
            case "1":
                pass
            case "2":
                pass
            case "3":
                listarProduto()
            case "4":
                pass
            case "0":
                return
            case _:
                print("Opção inválida")
                input()
                
# Path: src/layouts/menuAdicionarProduto.py