from src.classes.vendedor import Vendedor
from src.database.find_one import find_one
from src.classes.produto import Produto
from src.database.update_one import update_one
from src.utils.formatarTexto import formatarTexto_vermelho

def setarVendedorProduto(vendedor: Vendedor):
    try:
        for produto in vendedor.produtos:
            filtro = {"_id": produto["id"]}
            produtoJson = find_one("produto", filtro)
            if produtoJson:
                vendedorJson = {
                    "id": vendedor._id,
                    "nome": vendedor.nome
                }
                produto = Produto(vendedor=vendedorJson)
                result = update_one("produto", produto.toDict(), filtro)
                if result == None:
                    raise Exception("Erro ao setar vendedor do produto")
            else:
                raise Exception("Produto não encontrado")
    except Exception as e:
        print(f"Erro ao setar vendedor do produto: {formatarTexto_vermelho(str(e))}")
        input()
    except KeyboardInterrupt:
        return