from typing import Optional
from src.classes.produto import Produto
from src.utils.solicitarInput import solicitarInput
from src.utils.formatarTexto import formatarTexto_negrito, formatarTexto_vermelho

def criarProduto(isRequired: bool) -> Optional[Produto]:
    try:
        nome = solicitarInput(f"Digite o {formatarTexto_negrito("nome")} do produto: ", isRequired)
        descricao = solicitarInput(f"Digite a {formatarTexto_negrito("descrição")} do produto: ", isRequired)
        preco = float(solicitarInput(f"Digite o {formatarTexto_negrito("preço")} do produto: ", isRequired))
        estoque = int(solicitarInput(f"Digite o {formatarTexto_negrito("estoque")} do produto: ", isRequired))
        produto = Produto(nome=nome, descricao=descricao, preco=preco, estoque=estoque)
        produto.validate()
        return produto
    except Exception as e:
        print(f"\nErro ao criar produto: {formatarTexto_vermelho(str(e))}")
        input()
        return None
    except KeyboardInterrupt:
        return None
        
# Path: src/utils/criarProduto.py