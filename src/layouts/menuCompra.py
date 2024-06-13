from src.utils.limparTerminal import limparTerminal
from src.functions.cadastrarCompra import cadastrarCompra
from src.functions.listarCompra import listarCompra
from src.functions.atualizarCompra import atualizarCompra
from src.functions.deletarCompra import deletarCompra

def menuCompra():
    while True:
        limparTerminal()
        
        print("-=" * 20 + "-")
        print("Menu Compra")
        print("1 - Cadastrar Compra")
        print("2 - Listar Compras")
        print("3 - Atualizar Compra")
        print("4 - Deletar Compra")
        print("0 - Voltar")
        print("-=" * 20 + "-")
        
        opcao = input("\nDigite a opção desejada: ")
        
        match opcao:
            case "1":
                cadastrarCompra()
            case "2":
                listarCompra()
            case "3":
                atualizarCompra()
            case "4":
                deletarCompra()
            case "0":
                return
            case _:
                print("Opção inválida")
                input()