from src.classes.usuario import Usuario
from src.classes.vendedor import Vendedor
from src.classes.produto import Produto
from src.classes.compra import Compra

compra = {
    "_id": "1",
    "dataCompra": '2021-09-01',
    "valorTotal": 100.0,
    "usuario": {
        "_id": "1",
        "nome": "João",
        "endereco": "Rua 1",
    },
    "produtos": [
        {
            "_id": "1",
            "nome": "Produto 1",
            "preco": 10.0
        },
        {
            "_id": "2",
            "nome": "Produto 2",
            "preco": 20.0
        }
    ]
}

produto = {
    "_id": "1",
    "nome": "Produto 25",
    "descricao": "Descrição do produto 1",
    "preco": 10.0,
    "estoque": 10,
    "vendedor": {
        "_id": "1",
        "nome": "Vendedor 1",
    }
}

usuario = {
    "_id": "2",
    "nome": "Pedro Augusto",
    "endereco": "Rua 1",
    "rg": "123456789"
}

vendedor = {
    "_id": "1",
    "nome": "Vendedor 1",
    "rg": "123456789",
    "produtos": [
        {
            "_id": "1",
            "nome": "Produto 1",
            "preco": 10.0
        },
        {
            "_id": "2",
            "nome": "Produto 2",
            "preco": 20.0
        },
        {
            "_id": "3",
            "nome": "Produto 3",
            "preco": 30.0
        }
    ]
}

produtoObj = Produto.fromDict(produto)
vendedorObj = Vendedor.fromDict(vendedor)

vendedorObj.removeProduto("2")

print(vendedorObj)