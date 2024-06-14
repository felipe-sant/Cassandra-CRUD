from src.classes.usuario import Usuario
from src.utils.solicitarInput import solicitarInput
from typing import Optional
from src.utils.formatarTexto import formatarTexto_negrito, formatarTexto_vermelho

def criarUsuario(isRequired: bool) -> Optional[Usuario]:
    try:
        nome = solicitarInput(f"Digite o {formatarTexto_negrito("nome")} do usuário: ", isRequired)
        endereco = solicitarInput(f"Digite o {formatarTexto_negrito("endereço")} do usuário: ", isRequired)
        rg = solicitarInput(f"Digite o {formatarTexto_negrito("rg")} do usuário: ", isRequired)
        usuario = Usuario(nome=nome, endereco=endereco, rg=rg)
        usuario.validate()
        return usuario
    except Exception as e:
        print(f"\nErro ao criar usuário: {formatarTexto_vermelho(str(e))}")
        input()
        return None
    except KeyboardInterrupt:
        return None
    
# Path: src/utils/criarUsuario.py