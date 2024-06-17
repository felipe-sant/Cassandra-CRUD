from src.database.connection import get_collection
from src.utils.formatarTexto import formatarTexto_vermelho

def count_documents(colecaoNome: str, filtro: dict = None) -> int | None:
    try:
        colecao = get_collection(colecaoNome)
        count = colecao.count_documents(filtro, upper_bound=100)
        return count
    except Exception as e:
        print(f"\nErro ao contar documentos. {formatarTexto_vermelho(str(e))}")
        input()
        return 
    
# Path: src/database/count_documents.py