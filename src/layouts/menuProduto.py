from src.utils.limparTerminal import limparTerminal
from src.functions.cadastrarProduto import cadastrarProduto
from src.functions.listarProduto import listarProduto
from src.functions.atualizarProduto import atualizarProduto
from src.functions.deletarProduto import deletarProduto
from src.utils.formatarTexto import formatarTexto_negrito

def menuProduto():
    while True:
        limparTerminal()
        
        print("-=" * 20 + "-")
        print(formatarTexto_negrito("Menu Produto"))
        print("1 - Cadastrar Produto")
        print("2 - Listar Produtos")
        print("3 - Atualizar Produto")
        print("4 - Deletar Produto")
        print("0 - Voltar")
        print("-=" * 20 + "-")
        
        opcao = input("\nDigite a opção desejada: ")
        
        match opcao:
            case "1":
                cadastrarProduto()
            case "2":
                listarProduto()
            case "3":
                atualizarProduto()
            case "4":
                deletarProduto()
            case "0":
                return
            case _:
                print("Opção inválida")
                input()
                
# Path: src/layouts/menuProduto.py