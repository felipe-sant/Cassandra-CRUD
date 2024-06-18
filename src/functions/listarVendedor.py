from src.database.count_documents import count_documents
from src.utils.formatarTexto import (formatarTexto_italico, formatarTexto_negrito,
    formatarTexto_vermelho)
from src.database.find import find
from src.classes.vendedor import Vendedor
from src.database.find_one import find_one

def listarVendedor():
    try:
        total = count_documents("vendedor")
        if total == None:
            raise Exception("Erro ao conectar com o banco de dados.")
        if total == 0:
            raise Exception("Nenhum vendedor cadastrado.")
        nome = input(f"Digite o {formatarTexto_negrito("nome")} do vendedor: (deixe em branco para listar todos) ")
        if nome == "":
            vendedores = find("vendedor")
            if vendedores == None:
                raise Exception("Erro ao buscar vendedores")
            count = 1
            print()
            for vendedorJson in vendedores:
                print(formatarTexto_italico(f"{count}/{total} - Vendedor:"))
                vendedor = Vendedor.fromDict(vendedorJson)
                print(vendedor)
                input()
                count += 1
        else:
            filtro = {"nome": nome}
            vendedorJson = find_one("vendedor", filtro)
            if vendedorJson == None:
                raise Exception("Vendedor não encontrado.")
            vendedor = Vendedor.fromDict(vendedorJson)
            print()
            print(vendedor)
            input()
    except Exception as e:
        print(f"\nErro ao listar vendedores: {formatarTexto_vermelho(str(e))}")
        input()
    except KeyboardInterrupt:
        return
    
# Path: src/functions/listarVendedor.py