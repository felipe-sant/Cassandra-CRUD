from src.utils.criarProduto import criarProduto
from src.database.insert_one import insert_one
from src.utils.formatarTexto import formatarTexto_azul, formatarTexto_vermelho

def cadastrarProduto():
    try:
        produto = criarProduto(isRequired=True)
        if produto:
            result = insert_one("produto", produto.toDict())
            if result:
                print(f"\n{formatarTexto_azul(result)}")
                input()
    except Exception as e:
        print(f"\nErro ao cadastrar produto: {formatarTexto_vermelho(str(e))}")        
        input()
    except KeyboardInterrupt:
        return
    
# Path: src/functions/cadastrarProduto.py