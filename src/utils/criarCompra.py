from typing import Optional
from src.classes.compra import Compra
from src.utils.solicitarInput import solicitarInput
from src.utils.formatarTexto import formatarTexto_negrito, formatarTexto_vermelho

def criarCompra(isRequired: bool) -> Optional[Compra]:
    try:
        diaCompra = solicitarInput(f"Digite o {formatarTexto_negrito("dia")} da compra: ", isRequired)
        mesCompra = solicitarInput(f"Digite o {formatarTexto_negrito("mês")} da compra: ", isRequired)
        anoCompra = solicitarInput(f"Digite o {formatarTexto_negrito("ano")} da compra: ", isRequired)
        dataCompra = f"{diaCompra}/{mesCompra}/{anoCompra}"
        compra = Compra(dataCompra=dataCompra)
        compra.validate()
        return compra
    except Exception as e:
        print(f"\nErro ao criar compra: {formatarTexto_vermelho(str(e))}")
        input()
        return None
    except KeyboardInterrupt:
        return 
    
# Path: src/utils/criarCompra.py