from src.database.connection import get_collection
from src.utils.formatarTexto import formatarTexto_vermelho

def delete_all(colecaoNome: str) -> str | None:
    try:
        colecao = get_collection(colecaoNome)
        colecao.delete_all()
        return f"Dados da coleção '{colecaoNome}' deletados com sucesso!"
    except Exception as e:
        print(f"\nErro ao deletar dados da coleção '{colecaoNome}'. {formatarTexto_vermelho(str(e))}")
        input()
        return None
    
# Path: src/database/delete_all.py