from src.utils.criarUsuario import criarUsuario

if __name__ == "__main__":
    usuario = criarUsuario(False)
    
    if usuario:
        print("Usuário criado com sucesso")
        print(usuario.toDict())
    else:
        print("Falha ao criar usuário")