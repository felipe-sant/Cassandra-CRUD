from src.database.connection import get_collection

def delete_all(colecaoNome: str) -> str | None:
    try:
        colecao = get_collection(colecaoNome)
        colecao.delete_all()
        return f"Dados da coleção '{colecaoNome}' deletados com sucesso!"
    except Exception as e:
        print(f"\nErro ao deletar dados da coleção '{colecaoNome}'. {e}")
        input()
        return None