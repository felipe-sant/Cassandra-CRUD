from src.utils.criarUsuario import criarUsuario
from src.utils.formatarTexto import formatarTexto_azul, formatarTexto_vermelho
from src.database.insert_one import insert_one

def cadastrarUsuario():
    try:
        usuario = criarUsuario(isRequired=True)
        if usuario:
            result = insert_one("usuario", usuario.toDict()) 
            if result:
                print(f"\n{formatarTexto_azul(result)}")
                input()
        else:
            raise Exception("Usuário inválido")
    except Exception as e:
        print(f"\nErro ao cadastrar usuário: {formatarTexto_vermelho(str(e))}")
        input()
    except KeyboardInterrupt:
        return
    
# Path: src/functions/cadastrarUsuario.py