from src.utils.solicitarInput import solicitarInput
from src.utils.formatarTexto import (formatarTexto_azul, formatarTexto_negrito,
    formatarTexto_vermelho)
from src.database.find_one import find_one

def removerProduto(colecao: dict) -> dict:
    try:
        id = solicitarInput(f"Digite o {formatarTexto_negrito("id")} do produto: ")
        filtro = {"_id": id}
        produto = find_one("produto", filtro)
        if produto == None:
            raise Exception("Produto não encontrado")
        else:
            colecao.removeProduto(id)
            print(f"{formatarTexto_azul('Produto removido com sucesso!')}")
            input()
            return colecao  
    except Exception as e:
        print(f"\nErro ao remover produto: {formatarTexto_vermelho(str(e))}")
        input()
        return colecao
    except KeyboardInterrupt:
        return colecao