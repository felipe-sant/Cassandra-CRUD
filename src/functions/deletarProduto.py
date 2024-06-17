from src.utils.solicitarInput import solicitarInput
from src.utils.formatarTexto import (formatarTexto_azul, formatarTexto_negrito,
    formatarTexto_vermelho)
from src.database.delete_all import delete_all
from src.database.delete_one import delete_one

def deletarTodosProdutos():
    result = delete_all("produto")
    return result

def deletarProduto():
    try:
        id = solicitarInput(f"Digite o {formatarTexto_negrito("id")} do usuário que deseja deletar: ", isRequired=True)
        if id == "delete_all":
            result = deletarTodosProdutos()
        else:
            filtro = {"_id": id}
            result = delete_one("produto", filtro)
        if result:
            print(f"\n{formatarTexto_azul(result)}")
            input()
        else:
            raise Exception("Produto não encontrado")
    except Exception as e:
        print(f"\nErro ao deletar produto: {formatarTexto_vermelho(str(e))}")
        input()
    except KeyboardInterrupt:
        return
    
# Path: src/functions/deletarProduto.py