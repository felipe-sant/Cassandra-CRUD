from src.database.connection import get_collection

def find_one(colecaoNome: str, filtro: dict = None) -> dict | None:
    try:
        colecao = get_collection(colecaoNome)
        documento = colecao.find_one(filtro)
        return documento
    except Exception as e:
        print(f"\nErro ao buscar dados. {e}")
        input()
        return None