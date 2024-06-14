from src.database.connection import get_collection
from src.utils.formatarTexto import formatarTexto_vermelho

def delete_one(colecaoNome: str, filtro: dict) -> str | None:
    try:
        colecao = get_collection(colecaoNome)
        colecao.delete_one(filtro)
        return f"Dado deletado com sucesso!"
    except Exception as e:
        print(f"\nErro ao deletar dado. {formatarTexto_vermelho(str(e))}")
        input()
        return None
    
# Path: src/database/delete_one.py