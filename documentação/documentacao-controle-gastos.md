# Documentação do Projeto
## Sistema de Controle de Gastos Pessoais (Python)

---

## 1. Visão Geral

Um programa de terminal (linha de comando) que permite ao usuário registrar, visualizar, editar, excluir e analisar seus gastos pessoais, organizados por categoria e data. Os dados são salvos em arquivo, então nada se perde ao fechar o programa.

**Por que esse projeto:** ele foi escolhido porque cobre, na prática, todos os pilares da lógica de programação — sem exigir nenhuma biblioteca externa ou framework. É 100% Python puro.

---

## 2. Objetivos de Aprendizado

Ao concluir este projeto, você terá praticado:

- Estruturas condicionais (`if`, `elif`, `else`)
- Laços de repetição (`while`, `for`)
- Funções (criação, parâmetros, retorno)
- Listas e dicionários
- Leitura e escrita em arquivos (persistência de dados)
- Tratamento de erros (`try`/`except`)
- Validação de entrada do usuário
- Organização de código em módulos (arquivos separados)
- Lógica de menus interativos

---

## 3. Funcionalidades (Escopo)

### Obrigatórias (MVP — Produto Mínimo Viável)
1. **Adicionar gasto**: descrição, valor, categoria, data
2. **Listar gastos**: todos, ou filtrados por categoria/mês
3. **Editar gasto**: alterar um registro existente
4. **Excluir gasto**: remover um registro
5. **Resumo/Relatório**: total gasto, total por categoria, gasto médio
6. **Persistência**: salvar tudo em arquivo (JSON) para não perder dados ao fechar

### Extras (se quiser ir além depois do MVP)
- Definir um orçamento mensal e alertar quando ultrapassar
- Exportar relatório para `.csv` ou `.txt`
- Gráfico simples em texto (barras feitas com `*` ou `#`)
- Múltiplos usuários/perfis

---

## 4. Requisitos Técnicos

| Item | Definição |
|---|---|
| Linguagem | Python 3.x |
| Bibliotecas externas | Nenhuma obrigatória (apenas `json`, `os`, `datetime` — todas nativas) |
| Interface | Terminal (linha de comando), com menu numerado |
| Persistência | Arquivo `gastos.json` |
| Estrutura de dados | Cada gasto é um dicionário; todos os gastos ficam em uma lista |

### Formato de cada gasto (dicionário)
```python
{
    "id": 1,
    "descricao": "Mercado",
    "valor": 150.75,
    "categoria": "Alimentação",
    "data": "2026-09-16"
}
```

---

## 5. Estrutura de Arquivos Sugerida

```
controle-gastos/
│
├── main.py            # Ponto de entrada — mostra o menu e chama as funções
├── gastos.py          # Funções de lógica (adicionar, editar, excluir, listar)
├── arquivo.py         # Funções de salvar/carregar o arquivo JSON
├── relatorios.py       # Funções de cálculo (totais, resumo por categoria)
└── gastos.json         # Onde os dados ficam salvos (criado automaticamente)
```

> Começando: se preferir, dá pra fazer tudo em um único `main.py` primeiro, e só depois separar em arquivos — o que também é um ótimo exercício de organização de código.

---

## 6. Fluxo do Programa (Menu Principal)

```
======= CONTROLE DE GASTOS =======
1 - Adicionar gasto
2 - Listar gastos
3 - Editar gasto
4 - Excluir gasto
5 - Ver resumo/relatório
0 - Sair
===================================
Escolha uma opção:
```

O programa deve ficar em loop (`while True`) mostrando esse menu até o usuário escolher `0` para sair.

---

## 7. Roadmap de Desenvolvimento (Etapas Sugeridas)

**Etapa 1 — Estrutura básica**
- Criar o menu com `while True` e `if/elif`
- Fazer as opções apenas imprimirem uma mensagem (sem lógica real ainda)
- Testar se o menu funciona e se a opção "Sair" encerra o loop

**Etapa 2 — Adicionar gasto (em memória)**
- Criar uma lista vazia para guardar os gastos
- Implementar a opção "Adicionar", pedindo descrição, valor, categoria e data
- Validar que o valor digitado é um número (tratar erro se não for)
- Guardar como dicionário dentro da lista

**Etapa 3 — Listar gastos**
- Implementar a opção "Listar", percorrendo a lista com `for`
- Exibir de forma organizada (id, descrição, valor, categoria, data)

**Etapa 4 — Editar e Excluir**
- Pedir o id do gasto
- Buscar na lista e alterar ou remover
- Tratar o caso de id inexistente

**Etapa 5 — Resumo/Relatório**
- Somar todos os valores (total geral)
- Agrupar por categoria e somar (dicionário auxiliar)
- Exibir de forma clara

**Etapa 6 — Persistência em arquivo**
- Ao adicionar/editar/excluir, salvar a lista inteira no `gastos.json`
- Ao iniciar o programa, carregar os dados do arquivo (se existir)
- Tratar o caso do arquivo não existir ainda (primeira execução)

**Etapa 7 — Organização em módulos**
- Separar as funções em arquivos diferentes, como na estrutura sugerida
- Praticar `import`

**Etapa 8 — Melhorias extras (opcional)**
- Escolher um dos itens da seção "Extras" acima

---

## 8. Conceitos de Lógica Aplicados em Cada Etapa

| Etapa | Conceitos principais |
|---|---|
| 1 | `while`, `if/elif/else`, funções |
| 2 | listas, dicionários, `try/except`, `input()` |
| 3 | laço `for`, formatação de string (`f-string`) |
| 4 | busca em lista, condicionais, manipulação de listas |
| 5 | acumuladores, dicionários para agrupamento |
| 6 | módulo `json`, leitura/escrita de arquivo, `os.path.exists()` |
| 7 | módulos, `import`, organização de código |

---

## 9. Regras de Validação (Requisitos Não Funcionais)

- Valor do gasto não pode ser negativo ou não numérico
- Data deve seguir um formato consistente (ex: `AAAA-MM-DD`)
- Categoria pode ser texto livre ou uma lista fixa de opções (você decide)
- Se o usuário digitar uma opção de menu inválida, o programa deve avisar e mostrar o menu novamente (sem travar)

---

## 10. Como Testar Manualmente

1. Adicionar 3 ou 4 gastos de categorias diferentes
2. Listar e conferir se todos aparecem certos
3. Editar um gasto e conferir se a alteração foi salva
4. Excluir um gasto e conferir se sumiu da lista
5. Fechar o programa e abrir de novo — os dados devem continuar lá
6. Ver o resumo e conferir se os totais batem com a soma manual

---

## 11. Próximos Passos

Sugestão: comece pela **Etapa 1** e vá me mostrando o código conforme avança — assim consigo te apontar ajustes e explicar cada trecho, em vez de te entregar tudo pronto.
