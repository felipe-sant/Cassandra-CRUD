from src.utils.solicitarInput import solicitarInput
from src.utils.formatarTexto import (formatarTexto_azul, formatarTexto_negrito,
    formatarTexto_vermelho)
from src.database.delete_one import delete_one
from src.database.delete_all import delete_all

def deletarTodosUsuarios():
    result = delete_all("usuario")
    return result

def deletarUsuario():
    try:
        id = solicitarInput(f"Digite o {formatarTexto_negrito("id")} do usuário que deseja deletar: ", isRequired=True)
        if id == "delete_all":
            result = deletarTodosUsuarios()
        else:
            filtro = {"_id": id}
            result = delete_one("usuario", filtro)
        if result:
            print(f"\n{formatarTexto_azul(result)}")
            input()
        else:
            raise Exception("Usuário não encontrado")
    except Exception as e:
        print(f"\nErro ao deletar usuário: {formatarTexto_vermelho(str(e))}")
        input()
    except KeyboardInterrupt:
        return
    
# Path: src/functions/deletarUsuario.py