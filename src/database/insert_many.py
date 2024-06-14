from src.database.connection import get_collection

def insert_many(colecaoNome: str, dados: list[dict]) -> str | None:
    try:
        colecao = get_collection(colecaoNome)
        colecao.insert_many(dados)
        return f"Dados inseridos com sucesso!"
    except Exception as e:
        print(f"\nErro ao inserir dados. {e}")
        input()
        return None