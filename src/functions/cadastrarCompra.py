from src.utils.criarCompra import criarCompra
from src.functions.adicionarUsuario import adicionarUsuario
from src.database.insert_one import insert_one
from src.utils.formatarTexto import formatarTexto_azul, formatarTexto_vermelho
from src.layouts.menuCampoProdutos import menuCampoProdutos
from src.layouts.menuCampoUsuario import menuCampoUsuario

def cadastrarCompra():
    try:
        compra = criarCompra(isRequired=True)
        compra = menuCampoUsuario(compra)
        compra = menuCampoProdutos(compra)
        compra.calcularValorTotal()
        compra.validate()
        if compra:
            result = insert_one("compra", compra.toDict())
            if result:
                print(f"\n{formatarTexto_azul(result)}")
                input()
        else:
            raise Exception("Compra inválida")
    except Exception as e:
        print(f"\nErro ao cadastrar compra: {formatarTexto_vermelho(str(e))}")
        input()
    except KeyboardInterrupt:
        return

# Path: src/functions/cadastrarCompra.py