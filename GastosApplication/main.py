import json
from multiprocessing import Value
import os

ARQUIVO = "gastos.json"

gastos = []
categorias = [    
    "alimentação",
    "transporte",
    "moradia",
    "saúde",
    "educação",
    "lazer",
    "vestuário",
    "tecnologia",
    "casa",
    "cuidados pessoais",
    "presentes e doações",
    "outros",]

def salvar_gasto():
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(gastos, arquivo, indent=4)
        arquivo.close()

def adicionar_gasto():
    descricao = input("Digite a descrição do gasto: ")
    try:
        valor = float(input("Digite o valor: "))
        if valor > 0:
            categoria = input("Digite a categoria: ").lower()
            data = input("Digite a data (AAAA/MM/DD): ")
            pass
        else:
            print("Erro: Digite um número positivo!")
            return valor
        
    except ValueError:
        print("Erro: Digite um valor válido!")
        return 
    

    novo_gasto = {
        "id": len(gastos) + 1,
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria,
        "data": data
    }
    gastos.append(novo_gasto)
    salvar_gasto()
    print("Gasto adicionado com sucesso!")
    

print("=========MENU DE GASTOS=========")

while True:
    print()
    print("1 - Adicionar")
    print("2 - Listar")
    print("3 - Editar")
    print("4 - Excluir")
    print("5 - Resumo")
    print("0 - Sair")

    try:
        selecionar = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite apenas números!")
        continue

    if selecionar == 1:
        print("Você selecionou adicionar!")
        adicionar_gasto()
    elif selecionar == 2:
        print("Você selecionou listar!")
    elif selecionar == 3:
        print("Você selecionou editar!")
    elif selecionar == 4:
        print("Vcoê selecionou excluir!")
    elif selecionar == 5:
        print("Você selecionou resumo!")
    elif selecionar == 0:
        print("Você selecionou sair!")
        print()
        print()
        print()
        print("Saindo...")
        break
    else:
        print("Opção inválida. Selecione corretamente!")

