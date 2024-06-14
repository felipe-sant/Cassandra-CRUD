from typing import Optional
from src.classes.compra import Compra
from src.utils.solicitarInput import solicitarInput

def criarCompra(isRequired: bool) -> Optional[Compra]:
    try:
        diaCompra = solicitarInput("Digite o dia da compra: ", isRequired)
        mesCompra = solicitarInput("Digite o mês da compra: ", isRequired)
        anoCompra = solicitarInput("Digite o ano da compra: ", isRequired)
        dataCompra = f"{diaCompra}/{mesCompra}/{anoCompra}"
        compra = Compra(dataCompra=dataCompra)
        compra.validate()
        return compra
    except Exception as e:
        print(f"\nErro ao criar compra: {e}")
        input()
        return None
    except KeyboardInterrupt:
        return None