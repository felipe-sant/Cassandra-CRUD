from src.database.count_documents import count_documents
from src.utils.formatarTexto import (formatarTexto_italico, formatarTexto_negrito,
    formatarTexto_vermelho)
from src.database.find_one import find_one
from src.classes.compra import Compra
from src.database.find import find

def listarCompra():
    try:
        total = count_documents("compra")
        if total == None:
            raise Exception("Erro ao conectar com o banco de dados.")
        if total == 0:
            raise Exception("Nenhuma compra cadastrada.")
        dataCompra = input(f"Digite a {formatarTexto_negrito("data")} {formatarTexto_italico("(dd/mm/aaaa)")} da compra: (deixe em branco para listar todas) ")
        if dataCompra == "":
            compras = find("compra")
            if compras == None:
                raise Exception("Erro ao buscar compras.")
            count = 1
            print()
            for compraJson in compras:
                print(formatarTexto_italico(f"{count}/{total} - Compra:"))
                compra = Compra.fromDict(compraJson)
                print(compra)
                input()
                count += 1
        else:
            filtro = {"dataCompra": dataCompra}
            compraJson = find_one("compra", filtro)
            if compraJson == None:
                raise Exception("Compra não encontrada.")
            compra = Compra.fromDict(compraJson)
            print()
            print(compra)
            input()
    except Exception as e:
        print(f"\nErro ao listar compras: {formatarTexto_vermelho(str(e))}")
        input()
    except KeyboardInterrupt:
        return
    
# Path: src/functions/listarCompra.py