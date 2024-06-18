from src.utils.solicitarInput import solicitarInput
from src.utils.formatarTexto import (formatarTexto_azul, formatarTexto_negrito,
    formatarTexto_vermelho)
from src.classes.usuario import Usuario
from src.classes.produto import Produto
from src.database.insert_one import insert_one
from src.database.find_one import find_one

def cadastrarFavorito():
    try:
        id_usuario = solicitarInput(f"Digite o {formatarTexto_negrito("ID")} do {formatarTexto_negrito("Usuário")}: ", isRequired=True)
        usuarioJson = find_one("usuario", {"_id": id_usuario})
        if usuarioJson == None:
            raise Exception("Usuário não encontrado.")
        usuario = Usuario.fromDict(usuarioJson)
        
        id_produto = solicitarInput(f"Digite o {formatarTexto_negrito("ID")} do {formatarTexto_negrito("Produto")}: ", isRequired=True)
        produtoJson = find_one("produto", {"_id": id_produto})
        if produtoJson == None:
            raise Exception("Produto não encontrado.")
        produto = Produto.fromDict(produtoJson)
        
        favorito = {
            "id_usuario": usuario._id,
            "id_produto": produto._id
        }
        
        result = insert_one("favorito", favorito)
        
        if result:
            print(f"\n{formatarTexto_azul(result)}")
            input()
        
    except Exception as e:
        print(f"\nErro ao cadastrar favorito: {formatarTexto_vermelho(str(e))}")
        input()
    except KeyboardInterrupt:
        return
    
# Path: src/functions/cadastrarFavorito.py