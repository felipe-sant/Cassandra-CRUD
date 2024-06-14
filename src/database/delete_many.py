from src.database.connection import get_collection

def delete_many(colecaoNome: str, filtro: dict) -> str | None:
    try:
        colecao = get_collection(colecaoNome)
        colecao.delete_many(filtro)
        return f"Dados deletados com sucesso!"
    except Exception as e:
        print(f"\nErro ao deletar dados. {e}")
        input()
        return None