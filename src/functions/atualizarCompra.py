from src.utils.solicitarInput import solicitarInput
from src.utils.formatarTexto import (formatarTexto_azul, formatarTexto_negrito,
    formatarTexto_vermelho)
from src.database.find_one import find_one
from src.classes.compra import Compra
from src.utils.criarCompra import criarCompra
from src.layouts.menuCampoUsuario import menuCampoUsuario
from src.layouts.menuCampoProdutos import menuCampoProdutos
from src.database.update_one import update_one

def atualizarCompra():
    try:
        id = solicitarInput(f"Digite o {formatarTexto_negrito("id")} da compra que deseja atualizar: ", isRequired=True)
        filtro = {"_id": id}
        compra = find_one("compra", filtro)
        if compra == None:
            raise Exception("Compra não encontrada.")
        
        compra = Compra.fromDict(compra)
        compraUpdate = criarCompra(isRequired=False, compra=compra)
        
        opcao = input(f"\nDeseja atualizar o {formatarTexto_negrito("usuario")} da compra? (s/n): ")
        if opcao.lower() == "s":
            compraUpdate = menuCampoUsuario(compraUpdate)
            
        opcao = input(f"\nDeseja atualizar os {formatarTexto_negrito("produtos")} da compra? (s/n): ")
        if opcao.lower() == "s":
            compraUpdate.produtos = compra.produtos
            compraUpdate = menuCampoProdutos(compraUpdate)
            compraUpdate.calcularValorTotal()
            
        result = update_one("compra", compraUpdate.toDict(), filtro)
        if result:
            print(f"\n{formatarTexto_azul(result)}")
            input()
        else:
            raise Exception("Erro ao atualizar compra.")
        
    except Exception as e:
        print(f"\nErro ao atualizar compra: {formatarTexto_vermelho(str(e))}")
        input()
    except KeyboardInterrupt:
        return