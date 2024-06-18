from src.utils.criarVendedor import criarVendedor
from src.database.insert_one import insert_one
from src.utils.formatarTexto import formatarTexto_azul, formatarTexto_vermelho
from src.layouts.menuCampoProdutos import menuCampoProdutos
from src.functions.setarVendedorProdutos import setarVendedorProduto

def cadastrarVendedor():
    try:
        vendedor = criarVendedor(isRequired=True)
        opcao = input("\nDeseja adicionar produtos ao vendedor? (s/n): ")
        if opcao.lower() == "s":
            vendedor = menuCampoProdutos(vendedor)
        if vendedor:
            result = insert_one("vendedor", vendedor.toDict())
            if result:
                print(f"\n{formatarTexto_azul(result)}")
                input()
                setarVendedorProduto(vendedor)
        else:
            raise Exception("Vendedor inválido")
    except Exception as e:
        print(f"\nErro ao cadastrar usuário: {formatarTexto_vermelho(str(e))}")
        input()
    except KeyboardInterrupt:
        return
    
# Path: src/functions/cadastrarVendedor.py