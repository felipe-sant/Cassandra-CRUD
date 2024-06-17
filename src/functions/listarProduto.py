from src.database.count_documents import count_documents
from src.utils.formatarTexto import (formatarTexto_italico, formatarTexto_negrito,
    formatarTexto_vermelho)
from src.database.find import find
from src.classes.produto import Produto
from src.database.find_one import find_one

def listarProduto():
    try:
        total = count_documents("produto")
        if total == None:
            raise Exception("Erro ao conectar com o banco de dados.")
        if total == 0:
            raise Exception("Nenhum produto cadastrado.")
        
        nome = input(f"Digite o {formatarTexto_negrito("nome")} do produto: (deixe em branco para listar todos) ")
        if nome == "":
            produtos = find("produto")
            if produtos == None:
                raise Exception("Erro ao buscar produtos.")
            
            count = 1
            print()
            for produtoJson in produtos:
                print(formatarTexto_italico(f"{count}/{total} - Produto:"))
                produto = Produto.fromDict(produtoJson)
                print(produto)
                input()
                count += 1
        else:
            filtro = {"nome": nome}
            produtoJson = find_one("produto", filtro)
            if produtoJson == None:
                raise Exception("Produto não encontrado.")
            produto = Produto.fromDict(produtoJson)
            print()
            print(produto)
            input()
    except Exception as e:
        print(f"\nErro ao listar produtos: {formatarTexto_vermelho(str(e))}")
        input()
    except KeyboardInterrupt:
        return
    
# Path: src/functions/listarProduto.py