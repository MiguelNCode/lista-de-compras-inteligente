import json
from lista_de_compras_inteli_func import *


while True:
    clear()
    print('='*10 + " Lista de Compras " + '='*10)
    try:
        dado_inicial = []
        with open("lista_de_produtos.json", "x", encoding="utf-8") as arq:
            json.dump(dado_inicial, arq, indent=4, ensure_ascii=False)
    except:
        escolha_funcionalidade = int(input("[1] Adicionar Item\n[2] Remover Itens\n[3] Ver Itens\n[4] Filtrar Itens\n[5] Sair\nEscolha: "))

        with open("lista_de_produtos.json", "r", encoding="utf-8") as arq:
            dados = json.load(arq)

        match escolha_funcionalidade:
            case 1:
                clear()
                adicionar_item(dados)
            case 2:
                clear()
                remover_item(dados)
            case 3:
                clear()
                listar_itens(dados)
            case 4:
                clear()
                filtrar_itens(dados)
            case _:
                print(">> Programa Finalizado!")
                break