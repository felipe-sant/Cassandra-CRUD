from src.utils.limparTerminal import limparTerminal
from src.functions.listarProduto import listarProduto
from src.utils.formatarTexto import formatarTexto_negrito
from src.functions.listarUsuario import listarUsuario
from src.functions.cadastrarFavorito import cadastrarFavorito
from src.functions.removerFavorito import removerFavorito

def menuFavorito():
    while True:
        limparTerminal()
        
        print("--" * 21)
        print(formatarTexto_negrito("Menu Adicionar Produto"))
        print("1 - Adicionar Favorito")
        print("2 - Listar Usuários")
        print("3 - Listar Produtos")
        print("4 - Remover Favorito")
        print("0 - Concluir")
        print("--" * 21)
        
        opcao = input("\nDigite a opção desejada: ")
        
        match opcao:
            case "1":
                cadastrarFavorito()
            case "2":
                listarUsuario()
            case "3":
                listarProduto()
            case "4":
                removerFavorito()
            case "0":
                return
            case _:
                print("Opção inválida")
                input()
                
# Path: src/layouts/menuAdicionarProduto.py