from src.database.connection import get_collection
from src.utils.formatarTexto import formatarTexto_vermelho

def insert_many(colecaoNome: str, dados: list[dict]) -> str | None:
    try:
        colecao = get_collection(colecaoNome)
        colecao.insert_many(dados)
        return f"Dados inseridos com sucesso!"
    except Exception as e:
        print(f"\nErro ao inserir dados. {formatarTexto_vermelho(str(e))}")
        input()
        return None
    
# Path: src/database/insert_many.py