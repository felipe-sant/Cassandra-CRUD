from src.utils.solicitarInput import solicitarInput
from src.utils.formatarTexto import (formatarTexto_azul, formatarTexto_negrito,
    formatarTexto_vermelho)
from src.database.find_one import find_one
from src.utils.criarVendedor import criarVendedor
from src.database.update_one import update_one
from src.classes.vendedor import Vendedor
from src.layouts.menuCampoProdutos import menuCampoProdutos
from src.functions.setarVendedorProdutos import setarVendedorProduto

def atualizarVendedor():
    try:
        id = solicitarInput(f"Digite o {formatarTexto_negrito("id")} do vendedor que deseja atualizar: ", isRequired=True)
        filtro = {"_id": id}
        vendedor = find_one("vendedor", filtro)
        if vendedor == None:
            raise Exception("Vendedor não encontrado.")
        vendedor = Vendedor.fromDict(vendedor)
        vendedorUpdate = criarVendedor(isRequired=False, vendedor=vendedor)
        opcao = input(f"\nDeseja atualizar os {formatarTexto_negrito("produtos")} do vendedor? (s/n): ")
        if opcao.lower() == "s":
            vendedorUpdate.produtos = vendedor.produtos
            vendedorUpdate = menuCampoProdutos(vendedorUpdate)
            vendedor.produtos = vendedorUpdate.produtos
        result = update_one("vendedor", vendedorUpdate.toDict(), filtro)
        if result:
            print(f"\n{formatarTexto_azul(result)}")
            setarVendedorProduto(vendedor)
            input()
        else:
            raise Exception("Erro ao atualizar vendedor.")
    except Exception as e:
        print(f"\nErro ao atualizar vendedor: {formatarTexto_vermelho(str(e))}")
        input()
    except KeyboardInterrupt:
        return
    
# Path: src/functions/atualizarVendedor.py