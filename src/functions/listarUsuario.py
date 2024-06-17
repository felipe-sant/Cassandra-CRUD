from src.database.find import find
from src.classes.usuario import Usuario
from src.utils.formatarTexto import (formatarTexto_italico, formatarTexto_negrito,
    formatarTexto_vermelho)
from src.database.count_documents import count_documents
from src.database.find_one import find_one

def listarUsuario():
    try:
        total = count_documents("usuario")
        if total == None:
            raise Exception("Erro ao conectar com o banco de dados.")
        if total == 0:
            raise Exception("Nenhum usuário cadastrado.")
        nome = input(f"Digite o {formatarTexto_negrito("nome")} do usuário: (deixe em branco para listar todos) ")
        if nome == "":
            usuarios = find("usuario")
            if usuarios == None:
                raise Exception("Erro ao buscar usuários.")
            count = 1
            print()
            for usuarioJson in usuarios:
                print(formatarTexto_italico(f"{count}/{total} - Usuário:"))
                usuario = Usuario.fromDict(usuarioJson)
                print(usuario)
                input()
                count += 1
        else:
            filtro = {"nome": nome}
            usuarioJson = find_one("usuario", filtro)
            if usuarioJson == None:
                raise Exception("Usuário não encontrado.")
            usuario = Usuario.fromDict(usuarioJson)
            print()
            print(usuario)
            input()
    except Exception as e:
        print(f"\nErro ao listar usuários: {formatarTexto_vermelho(str(e))}")
        input()
    except KeyboardInterrupt:
        return
    
# Path: src/functions/listarUsuario.py