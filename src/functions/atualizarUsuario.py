from src.utils.solicitarInput import solicitarInput
from src.utils.formatarTexto import (formatarTexto_azul, formatarTexto_negrito,
    formatarTexto_vermelho)
from src.utils.criarUsuario import criarUsuario
from src.database.update_one import update_one

def atualizarUsuario():
    try:
        id = solicitarInput(f"Digite o {formatarTexto_negrito("id")} do usuário que deseja atualizar: ", isRequired=True)
        filtro = {"_id": id}
        usuarioUpdate = criarUsuario(isRequired=False)
        result = update_one("usuario", usuarioUpdate.toDict(), filtro)
        if result:
            print(f"\n{formatarTexto_azul(result)}")
            input()
        else:
            raise Exception("Erro ao atualizar usuário.")
    except Exception as e:
        print(f"\nErro ao atualizar usuário: {formatarTexto_vermelho(str(e))}")
        input()
    except KeyboardInterrupt:
        return
    
# Path: src/functions/atualizarUsuario.py