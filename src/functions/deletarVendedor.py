from src.database.delete_all import delete_all
from src.utils.solicitarInput import solicitarInput
from src.utils.formatarTexto import (formatarTexto_azul, formatarTexto_negrito,
    formatarTexto_vermelho)
from src.database.find_one import find_one
from src.database.delete_one import delete_one

def deletarTodosVendedores():
    result = delete_all("vendedor")
    return result

def deletarVendedor():
    try:
        id = solicitarInput(f"Digite o {formatarTexto_negrito('id')} do vendedor que deseja deletar: ", isRequired=True)
        if id == "delete_all":
            result = deletarTodosVendedores()
        else:
            filtro = {"_id": id}
            vendedor = find_one("vendedor", filtro)
            if vendedor == None:
                raise Exception("Vendedor não encontrado.")
            result = delete_one("vendedor", filtro)    
        if result:
            print(f"\n{formatarTexto_azul(result)}")
            input()
        else:
            raise Exception("Vendedor não encontrado")
    except Exception as e:
        print(f"\nErro ao deletar vendedor: {formatarTexto_vermelho(str(e))}")
        input()
    except KeyboardInterrupt:
        return    
    
# Path: src/functions/deletarVendedor.py