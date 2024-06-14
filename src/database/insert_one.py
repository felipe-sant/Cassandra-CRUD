from src.database.connection import get_collection
from src.utils.formatarTexto import formatarTexto_vermelho

def insert_one(colecaoNome: str, dado: dict) -> str | None:
    try:
        colecao = get_collection(colecaoNome)
        colecao.insert_one(dado)
        return f"Dado adicionado com sucesso!"
    except Exception as e:
        print(f"\nErro ao adicionar dado. {formatarTexto_vermelho(str(e))}")
        input()
        return None
    
# Path: src/database/insert_one.py