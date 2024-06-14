from typing import Optional
from src.classes.produto import Produto
from src.utils.solicitarInput import solicitarInput

def criarProduto(isRequired: bool) -> Optional[Produto]:
    try:
        nome = solicitarInput("Digite o nome do produto: ", isRequired)
        descricao = solicitarInput("Digite a descrição do produto: ", isRequired)
        preco = float(solicitarInput("Digite o preço do produto: ", isRequired))
        estoque = int(solicitarInput("Digite o estoque do produto: ", isRequired))
        produto = Produto(nome=nome, descricao=descricao, preco=preco, estoque=estoque)
        produto.validate()
        return produto
    except Exception as e:
        print(f"\nErro ao criar produto: {e}")
        input()
        return None
    except KeyboardInterrupt:
        return None
        