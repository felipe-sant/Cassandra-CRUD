from src.classes.usuario import Usuario
from src.utils.solicitarInput import solicitarInput
from typing import Optional

def criarUsuario(isRequired: bool) -> Optional[Usuario]:
    try:
        nome = solicitarInput("Digite o nome do usuário: ", isRequired)
        endereco = solicitarInput("Digite o endereço do usuário: ", isRequired)
        rg = solicitarInput("Digite o RG do usuário: ", isRequired)
        usuario = Usuario(nome=nome, endereco=endereco, rg=rg)
        usuario.validate()
        return usuario
    except Exception as e:
        print(f"\nErro ao criar usuário: {e}")
        input()
        return None
    except KeyboardInterrupt:
        return None