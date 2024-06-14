from src.database.connection import get_collection

def update_one(colecaoNome: str, dado: dict, filtro: dict) -> str | None:
    try:
        colecao = get_collection(colecaoNome)
        colecao.update_one(filtro, {"$set": dado})
        return f"Dado atualizado com sucesso!"
    except Exception as e:
        print(f"\nErro ao atualizar dado. {e}")
        input()
        return None