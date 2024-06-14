from src.database.connection import get_collection

def delete_one(colecaoNome: str, filtro: dict) -> str | None:
    try:
        colecao = get_collection(colecaoNome)
        colecao.delete_one(filtro)
        return f"Dado deletado com sucesso!"
    except Exception as e:
        print(f"\nErro ao deletar dado. {e}")
        input()
        return None