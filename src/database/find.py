from src.database.connection import get_collection
from src.utils.formatarTexto import formatarTexto_vermelho

def find(colecaoNome: str, filtro: dict = None) -> list[dict] | None:
    try:
        colecao = get_collection(colecaoNome)
        dados = colecao.find(filtro)
        return dados
    except Exception as e:
        print(f"\nErro ao buscar dados. {formatarTexto_vermelho(str(e))}")
        return None
    
# Path: src/database/find.py