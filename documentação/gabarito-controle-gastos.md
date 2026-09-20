# Gabarito — Sistema de Controle de Gastos Pessoais

> Tente resolver cada exercício sozinho antes de olhar aqui. Isso é só para conferir ou destravar se ficar preso.

---

## Estrutura de Pastas Final (após o Exercício 11)

```
controle-gastos/
│
├── main.py
├── gastos.py
├── arquivo.py
├── relatorios.py
└── gastos.json          (gerado automaticamente ao rodar o programa)
```

---

## Exercícios 1 a 10 (tudo em `main.py`)

```python
import json
import os

ARQUIVO = "gastos.json"
gastos = []


# ---------- Exercício 10: carregar dados ao iniciar ----------
def carregar_dados():
    global gastos
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            gastos = json.load(f)
    else:
        gastos = []


# ---------- Exercício 9: salvar dados ----------
def salvar_dados():
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(gastos, f, indent=4, ensure_ascii=False)


# ---------- Exercício 3: validar valor ----------
def pedir_valor():
    while True:
        try:
            valor = float(input("Valor: R$"))
            if valor < 0:
                print("O valor não pode ser negativo. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("Valor inválido. Digite um número (ex: 50.90).")


# ---------- Exercício 2: adicionar gasto ----------
def adicionar_gasto():
    descricao = input("Descrição: ")
    valor = pedir_valor()
    categoria = input("Categoria: ")
    data = input("Data (AAAA-MM-DD): ")

    novo_gasto = {
        "id": len(gastos) + 1,
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria,
        "data": data
    }
    gastos.append(novo_gasto)
    salvar_dados()
    print("Gasto adicionado com sucesso!")


# ---------- Exercício 4: listar gastos ----------
def listar_gastos():
    if not gastos:
        print("Nenhum gasto cadastrado ainda.")
        return

    for gasto in gastos:
        print(f"[{gasto['id']}] {gasto['descricao']} - "
              f"R${gasto['valor']:.2f} - {gasto['categoria']} - {gasto['data']}")


# ---------- Exercício 5: editar gasto ----------
def editar_gasto():
    id_busca = int(input("ID do gasto a editar: "))

    for gasto in gastos:
        if gasto["id"] == id_busca:
            gasto["descricao"] = input("Nova descrição: ")
            gasto["valor"] = pedir_valor()
            gasto["categoria"] = input("Nova categoria: ")
            gasto["data"] = input("Nova data (AAAA-MM-DD): ")
            salvar_dados()
            print("Gasto atualizado com sucesso!")
            return

    print("Gasto não encontrado.")


# ---------- Exercício 6: excluir gasto ----------
def excluir_gasto():
    id_busca = int(input("ID do gasto a excluir: "))

    for gasto in gastos:
        if gasto["id"] == id_busca:
            gastos.remove(gasto)
            salvar_dados()
            print("Gasto excluído com sucesso!")
            return

    print("Gasto não encontrado.")


# ---------- Exercícios 7 e 8: resumo/relatório ----------
def mostrar_resumo():
    if not gastos:
        print("Nenhum gasto cadastrado ainda.")
        return

    total_geral = 0
    totais_categoria = {}

    for gasto in gastos:
        total_geral += gasto["valor"]

        categoria = gasto["categoria"]
        if categoria in totais_categoria:
            totais_categoria[categoria] += gasto["valor"]
        else:
            totais_categoria[categoria] = gasto["valor"]

    print(f"\nTotal gasto: R${total_geral:.2f}")
    print("Totais por categoria:")
    for categoria, total in totais_categoria.items():
        print(f"  {categoria}: R${total:.2f}")


# ---------- Exercício 1: menu principal ----------
def main():
    carregar_dados()

    while True:
        print("\n======= CONTROLE DE GASTOS =======")
        print("1 - Adicionar gasto")
        print("2 - Listar gastos")
        print("3 - Editar gasto")
        print("4 - Excluir gasto")
        print("5 - Ver resumo/relatório")
        print("0 - Sair")
        print("===================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_gasto()
        elif opcao == "2":
            listar_gastos()
        elif opcao == "3":
            editar_gasto()
        elif opcao == "4":
            excluir_gasto()
        elif opcao == "5":
            mostrar_resumo()
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
```

---

## Exercício 11 — Separado em módulos

### `arquivo.py`
```python
import json
import os

ARQUIVO = "gastos.json"


def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_dados(gastos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(gastos, f, indent=4, ensure_ascii=False)
```

### `gastos.py`
```python
from arquivo import salvar_dados


def pedir_valor():
    while True:
        try:
            valor = float(input("Valor: R$"))
            if valor < 0:
                print("O valor não pode ser negativo. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("Valor inválido. Digite um número (ex: 50.90).")


def adicionar_gasto(gastos):
    descricao = input("Descrição: ")
    valor = pedir_valor()
    categoria = input("Categoria: ")
    data = input("Data (AAAA-MM-DD): ")

    novo_gasto = {
        "id": len(gastos) + 1,
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria,
        "data": data
    }
    gastos.append(novo_gasto)
    salvar_dados(gastos)
    print("Gasto adicionado com sucesso!")


def listar_gastos(gastos):
    if not gastos:
        print("Nenhum gasto cadastrado ainda.")
        return

    for gasto in gastos:
        print(f"[{gasto['id']}] {gasto['descricao']} - "
              f"R${gasto['valor']:.2f} - {gasto['categoria']} - {gasto['data']}")


def editar_gasto(gastos):
    id_busca = int(input("ID do gasto a editar: "))

    for gasto in gastos:
        if gasto["id"] == id_busca:
            gasto["descricao"] = input("Nova descrição: ")
            gasto["valor"] = pedir_valor()
            gasto["categoria"] = input("Nova categoria: ")
            gasto["data"] = input("Nova data (AAAA-MM-DD): ")
            salvar_dados(gastos)
            print("Gasto atualizado com sucesso!")
            return

    print("Gasto não encontrado.")


def excluir_gasto(gastos):
    id_busca = int(input("ID do gasto a excluir: "))

    for gasto in gastos:
        if gasto["id"] == id_busca:
            gastos.remove(gasto)
            salvar_dados(gastos)
            print("Gasto excluído com sucesso!")
            return

    print("Gasto não encontrado.")
```

### `relatorios.py`
```python
def mostrar_resumo(gastos):
    if not gastos:
        print("Nenhum gasto cadastrado ainda.")
        return

    total_geral = 0
    totais_categoria = {}

    for gasto in gastos:
        total_geral += gasto["valor"]

        categoria = gasto["categoria"]
        if categoria in totais_categoria:
            totais_categoria[categoria] += gasto["valor"]
        else:
            totais_categoria[categoria] = gasto["valor"]

    print(f"\nTotal gasto: R${total_geral:.2f}")
    print("Totais por categoria:")
    for categoria, total in totais_categoria.items():
        print(f"  {categoria}: R${total:.2f}")
```

### `main.py`
```python
from arquivo import carregar_dados
from gastos import adicionar_gasto, listar_gastos, editar_gasto, excluir_gasto
from relatorios import mostrar_resumo


def main():
    gastos = carregar_dados()

    while True:
        print("\n======= CONTROLE DE GASTOS =======")
        print("1 - Adicionar gasto")
        print("2 - Listar gastos")
        print("3 - Editar gasto")
        print("4 - Excluir gasto")
        print("5 - Ver resumo/relatório")
        print("0 - Sair")
        print("===================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_gasto(gastos)
        elif opcao == "2":
            listar_gastos(gastos)
        elif opcao == "3":
            editar_gasto(gastos)
        elif opcao == "4":
            excluir_gasto(gastos)
        elif opcao == "5":
            mostrar_resumo(gastos)
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
```
