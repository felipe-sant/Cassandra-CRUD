from typing import Optional
from src.classes.vendedor import Vendedor
from src.utils.solicitarInput import solicitarInput
from src.utils.formatarTexto import formatarTexto_negrito, formatarTexto_vermelho

def criarVendedor(isRequired: bool) -> Optional[Vendedor]:
    try:
        nome = solicitarInput(f"Digite o {formatarTexto_negrito("nome")} do vendedor: ", isRequired)
        rg = solicitarInput(f"Digite o {formatarTexto_negrito("rg")} do vendedor: ", isRequired)
        vendedor = Vendedor(nome=nome, rg=rg)
        vendedor.validate()
        return vendedor
    except Exception as e:
        print(f"\nErro ao criar vendedor: {formatarTexto_vermelho(str(e))}")
        input()
        return None
    except KeyboardInterrupt:
        return None
    
# Path: src/utils/criarVendedor.py