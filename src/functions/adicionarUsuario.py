from src.classes.compra import Compra
from src.utils.solicitarInput import solicitarInput
from src.utils.formatarTexto import (formatarTexto_azul, formatarTexto_negrito,
    formatarTexto_vermelho)
from src.database.find_one import find_one
from src.classes.usuario import Usuario

def adicionarUsuario(compra: Compra) -> None:
    try:
        id = solicitarInput(f"Digite o {formatarTexto_negrito("id")} do usuário: ")
        filtro = {"_id": id}
        usuario = find_one("usuario", filtro)
        if usuario == None:
            raise Exception("Usuário não encontrado")
        else:
            usuario = Usuario.fromDict(usuario)
            compra.setUsuario(usuario)
            print(f"{formatarTexto_azul('\nUsuário adicionado com sucesso!')}")
            input()
            return compra
    except Exception as e:
        print(f"Erro ao adicionar usuário: {formatarTexto_vermelho(str(e))}")
        input()
        return compra
    except KeyboardInterrupt:
        return
    
# Path: src/functions/adicionarUsuario.py