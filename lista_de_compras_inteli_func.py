from lista_de_compras_inteli_class import Produto
import json
from os import system, name
from time import sleep


# Adicionar valor ao JSON
def adicionar_json(dados_json):
    with open("lista_de_produtos.json", "w", encoding="utf-8") as arq:
        json.dump(dados_json, arq, indent=4, ensure_ascii=False)


# Método que limpa o terminal
def clear():
    SO = name
    if SO == "win32":
        system("cls")
    else:
        system("clear")


# Método que intoruduz a escolha da categoria do Produto
def tipo_do_prod():
    while True:
        print()
        print('='*10 + " CATEGORIA " + '='*10)
        tip = int(input("[1] Alimentício\n[2] Higiene\n[3] Bebidas\n[4] Outros\nEscolha: "))
        match tip:
            case 1:
                return "alimentício"
            case 2:
                return "higiene"
            case 3:
                return "bebidas"
            case 4:
                return "outros"
            case _:
                continue


# Método que retorna um dicionário ao JSON com informações do produto
def adicionar_item(dados):
    produto_cad = Produto(input("Nome: "), float(input("Preço: ")), tipo_do_prod(), int(input("\nQuantidade: ")), 0)
    produto_cad.tot = produto_cad.price * produto_cad.unid
    caracteristica_prod = {"name": produto_cad.name.upper(), "price": produto_cad.price, "type": produto_cad.type.upper(), "unid": produto_cad.unid, "total": produto_cad.tot}

    dados.append(caracteristica_prod)

    adicionar_json(dados)
    
    print("Adicinado a lista...")
    sleep(3)


# Método que remove as unid dos produtos
def remover_item(dados):


    # Método que simplifica a remoção do produto se ele não tiver unidades
    def remover_produto_completo():
        if valor["unid"] <= 0:
            dados.pop(ind)
            print("Produto removido por falta de quantidade!")

    while True:
        tem = False
        item_remover = input("Produto: ").upper()
        quantidade = int(input("Unidades [-1 para todas]: "))
        conta_total = lambda val: val["unid"] * val["price"]
        
        for ind, valor in enumerate(dados):
            if item_remover == valor["name"]:
                tem = True
                certeza = input(f"Você tem certeza que deseja remover {quantidade} unidades de {item_remover} [S/N]? ")
                if not certeza:
                    continue
                elif certeza and quantidade <= -1:
                    valor["unid"] = 0
                    print("Todas as unidades removidas...")

                    remover_produto_completo()

                else:
                    valor["unid"] -= quantidade
                    valor["total"] = conta_total(valor)

                    print(f"{quantidade} unidades foram removidas de {valor["name"]}" if quantidade > 1 else f"{quantidade} unidade foi removida de {valor["name"]}")
                    
                    remover_produto_completo()
            
        if not tem:
            print("Produto não está presente na lista...")

        adicionar_json(dados)

        sleep(5)
        break
        

# Método que mostra os valores
def listar_itens(dados):
    clear()
    if not dados:
        print("Lista vazia! Adicione contéudos antes de ver os valores...")
        sleep(3)
    else:
        for ind, valor in enumerate(dados):
            print(f"{ind+1}º {valor["name"].title()}:\n Tipo: {valor["type"].title()}\n Preço: {valor["price"]}\n Unidades: {valor["unid"]}\n Total: {valor["total"]}")
            print()

        input("Pressione ENTER para sair: ")


# Método que filtra os valores retornando uma lista com esse filtro e mostrando-a
def filtrar_itens(dados):
    escolha = int(input("[1] Valor\n[2] Alfabética\n[3] Categoria\nEscolha: "))
    match escolha:
        case 1:
            clear()
            escolha_ordem = int(input("[1] Crescente\n[2] Decrescente\nEscolha: "))
            match escolha_ordem:
                case 1:
                    valor_dados = sorted(dados, key=lambda valor: valor["total"])
                    listar_itens(valor_dados)
                case 2:
                    valor_dados = sorted(dados, key=lambda valor: valor["total"], reverse=True)
                    listar_itens(valor_dados)
        case 2:
            alfabetic_dados = sorted(dados, key=lambda valor: valor["name"])
            listar_itens(alfabetic_dados)
        case 3:
            clear()
            escolha_categoria = int(input("[1] Alimentício\n[2] Higiene\n[3] Bebidas\n[4] Outros\nEscolha: "))
            match escolha_categoria:
                case 1:
                    alimentos_dados = filter(lambda x: x["type"] == "ALIMENTÍCIO", dados)
                    listar_itens(alimentos_dados)
                case 2:
                    higiene_dados = filter(lambda x: x["type"] == "HIGIENE", dados)
                    listar_itens(higiene_dados)
                case 3:
                    bebidas_dados = filter(lambda x: x["type"] == "BEBIDAS", dados)
                    listar_itens(bebidas_dados)
                case 4:
                    outros_dados = filter(lambda x: x["type"] == "OUTROS", dados)
                    listar_itens(outros_dados)