from src.database.connection import get_collection
from src.utils.formatarTexto import formatarTexto_vermelho

def find_one(colecaoNome: str, filtro: dict = None) -> dict | None:
    try:
        colecao = get_collection(colecaoNome)
        documento = colecao.find_one(filtro)
        return documento
    except Exception as e:
        print(f"\nErro ao buscar dados. {formatarTexto_vermelho(str(e))}")
        input()
        return None
    
# Path: src/database/find_one.py