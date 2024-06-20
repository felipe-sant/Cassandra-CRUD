from src.database.delete_all import delete_all
from src.utils.solicitarInput import solicitarInput
from src.utils.formatarTexto import (formatarTexto_azul, formatarTexto_negrito,
    formatarTexto_vermelho)
from src.database.find_one import find_one
from src.database.delete_one import delete_one

def deletarTodasCompras():
    result = delete_all("compra")
    return result

def deletarCompra():
    try:
        id = solicitarInput(f"Digite o {formatarTexto_negrito("id")} da compra que deseja deletar: ", isRequired=True)
        if id == "delete_all":
            result = deletarTodasCompras()
        else:
            filtro = {"_id": id}
            compra = find_one("compra", filtro)
            if compra == None:
                raise Exception("Compra não encontrada.")
            result = delete_one("compra", filtro)
        if result:
            print(f"\n{formatarTexto_azul(result)}")
            input()
        else:
            raise Exception("Compra não encontrada")
    except Exception as e:
        print(f"\nErro ao deletar compra: {formatarTexto_vermelho(str(e))}")
        input()
    except KeyboardInterrupt:
        return
    
# Path: src/functions/deletarCompra.py