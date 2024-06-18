from src.utils.solicitarInput import solicitarInput
from src.utils.formatarTexto import (formatarTexto_azul, formatarTexto_negrito,
    formatarTexto_vermelho)
from src.database.find_one import find_one
from src.classes.produto import Produto

def adicionarProduto(colecao: dict) -> dict:
    try:
        id = solicitarInput(f"Digite o {formatarTexto_negrito("id")} do produto: ")
        filtro = {"_id": id}
        produto = find_one("produto", filtro)
        if produto == None:
            raise Exception("Produto não encontrado")
        else:
            produto = Produto.fromDict(produto)
            colecao.addProduto(produto)
            print(f"{formatarTexto_azul('\nProduto adicionado com sucesso!')}")
            input()
            return colecao
    except Exception as e:
        print(f"Erro ao adicionar produto: {formatarTexto_vermelho(str(e))}")
        input()
        return colecao
    except KeyboardInterrupt:
        return