from src.utils.solicitarInput import solicitarInput
from src.utils.formatarTexto import (formatarTexto_azul, formatarTexto_negrito,
    formatarTexto_vermelho)
from src.utils.criarProduto import criarProduto
from src.database.update_one import update_one
from src.database.find_one import find_one

def atualizarProduto():
    try:
        id = solicitarInput(f"Digite o {formatarTexto_negrito("id")} do produto que deseja atualizar: ", isRequired=True)
        filtro = {"_id": id}
        produto = find_one("produto", filtro)
        if not produto:
            raise Exception("Produto não encontrado.")
        produtoUpdate = criarProduto(isRequired=False)
        result = update_one("produto", produtoUpdate.toDict(), filtro)
        if result:
            print(f"\n{formatarTexto_azul(result)}")
            input()
        else:
            raise Exception("Erro ao atualizar produto.")
    except Exception as e:
        print(f"\nErro ao atualizar produto: {formatarTexto_vermelho(str(e))}")
        input()
    except KeyboardInterrupt:
        return
    
# Path: src/funcitons/atualizarProduto.py