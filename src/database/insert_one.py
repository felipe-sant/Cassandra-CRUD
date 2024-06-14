from src.database.connection import get_collection

def insert_one(colecaoNome: str, dado: dict) -> str | None:
    try:
        colecao = get_collection(colecaoNome)
        colecao.insert_one(dado)
        return f"Dado adicionado com sucesso!"
    except Exception as e:
        print(f"\nErro ao adicionar dado. {e}")
        input()
        return None