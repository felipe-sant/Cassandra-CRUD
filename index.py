from src.database.find import find
from src.utils.limparTerminal import limparTerminal

print()
usuarios = find("usuario")
# if usuario:
#     print(usuario)
#     input()
if usuarios:
    for usuario in usuarios:
        print(usuario)
        input()
else:
    print("Nenhum usuário encontrado.")
    input()
    
limparTerminal()