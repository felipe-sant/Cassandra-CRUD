from src.utils.limparTerminal import limparTerminal
from src.functions.cadastrarUsuario import cadastrarUsuario
from src.functions.listarUsuario import listarUsuario
from src.functions.atualizarUsuario import atualizarUsuario
from src.functions.deletarUsuario import deletarUsuario
from src.layouts.menuAdicionarProduto import menuAdicionarProduto

def menuUsuario():
    while True:
        limparTerminal()
        
        print("-=" * 20 + "-")
        print("Menu Usuário")
        print("1 - Cadastrar Usuário")
        print("2 - Listar Usuários")
        print("3 - Atualizar Usuário")
        print("4 - Deletar Usuário")
        print("5 - Adicionar favorito")
        print("0 - Voltar")
        print("-=" * 20 + "-")
        
        opcao = input("\nDigite a opção desejada: ")
        
        match opcao:
            case "1":
                cadastrarUsuario()
            case "2":
                listarUsuario()
            case "3":
                atualizarUsuario()
            case "4":
                deletarUsuario()
            case "5":
                menuAdicionarProduto(None, False)
            case "0":
                return
            case _:
                print("Opção inválida")
                input()