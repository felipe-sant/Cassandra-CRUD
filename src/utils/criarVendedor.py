from typing import Optional
from src.classes.vendedor import Vendedor
from src.utils.solicitarInput import solicitarInput

def criarVendedor(isRequired: bool) -> Optional[Vendedor]:
    try:
        nome = solicitarInput("Digite o nome do vendedor: ", isRequired)
        rg = solicitarInput("Digite o RG do vendedor: ", isRequired)
        vendedor = Vendedor(nome=nome, rg=rg)
        vendedor.validate()
        return vendedor
    except Exception as e:
        print(f"\nErro ao criar vendedor: {e}")
        input()
        return None
    except KeyboardInterrupt:
        return None