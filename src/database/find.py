from src.database.connection import get_collection

def find(colecaoNome: str, filtro: dict = None) -> list[dict] | None:
    try:
        colecao = get_collection(colecaoNome)
        dados = colecao.find(filtro)
        return dados
    except Exception as e:
        print(e)
        return None