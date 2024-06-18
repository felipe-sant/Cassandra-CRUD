from src.classes.usuario import Usuario
from src.database.find import find
from src.database.find_one import find_one
from src.classes.produto import Produto
from src.utils.formatarTexto import formatarTexto_vermelho

def listarFavorito(usuario: Usuario):
    try:
        filtro = { "id_usuario": usuario._id }
        
        favoritos = find("favorito", filtro)
        
        if favoritos == None:
            raise Exception(f"Erro ao buscar favoritos")
        
        for favorito in favoritos:
            filtro = { "_id": favorito["id_produto"] }
            produtoJson = find_one("produto", filtro)
            if produtoJson != None:
                produto = Produto(
                    _id=produtoJson["_id"],
                    nome=produtoJson["nome"],
                    descricao=produtoJson["descricao"]
                )
                print(produto)
    except Exception as e:
        print(f"Erro ao listar favorito: {formatarTexto_vermelho(str(e))}")
        input()
    except KeyboardInterrupt:
        return
    
# Path: src/functions/listarFavorito.py