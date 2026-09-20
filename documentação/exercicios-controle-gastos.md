# Exercícios — Sistema de Controle de Gastos Pessoais

Faça um exercício de cada vez, na ordem. Cada um usa o que foi construído no anterior. Só passe para o próximo quando o atual estiver funcionando.

> Trabalhe tudo em um único arquivo `main.py` por enquanto — a separação em módulos é o último exercício.

---

## Exercício 1 — Menu básico

**Objetivo:** criar o esqueleto do programa: um menu que fica em loop até o usuário sair.

**Requisitos:**
- Use `while True` para manter o menu aparecendo
- Mostre as opções: `1 - Adicionar`, `2 - Listar`, `3 - Editar`, `4 - Excluir`, `5 - Resumo`, `0 - Sair`
- Use `input()` para capturar a escolha
- Use `if/elif/else` para tratar cada opção — por enquanto, cada uma só imprime uma frase (ex: `"Você escolheu Adicionar"`)
- A opção `0` deve encerrar o loop (`break`)
- Se digitar algo que não é uma opção válida, mostre uma mensagem de erro e repita o menu

**Teste esperado:** rodar o programa, escolher cada opção e ver a mensagem correspondente aparecer, e escolher `0` para sair sem erro.

---

## Exercício 2 — Adicionar gasto (em memória)

**Objetivo:** implementar de verdade a opção "Adicionar".

**Requisitos:**
- Crie uma lista vazia `gastos = []` antes do loop do menu
- Quando escolher "Adicionar", peça: descrição, valor, categoria e data (pode ser texto livre por enquanto)
- Guarde cada gasto como um dicionário com as chaves: `id`, `descricao`, `valor`, `categoria`, `data`
- O `id` deve ser gerado automaticamente (ex: `len(gastos) + 1`)
- Adicione o dicionário na lista `gastos`
- Ao final, mostre uma confirmação (ex: `"Gasto adicionado com sucesso!"`)

**Teste esperado:** adicionar 2 ou 3 gastos seguidos, sem erro, e cada um com um `id` diferente.

---

## Exercício 3 — Validar o valor digitado

**Objetivo:** garantir que o programa não quebre se o usuário digitar um valor inválido.

**Requisitos:**
- Ao pedir o valor do gasto, use `try/except` para tentar converter para `float`
- Se falhar (ex: usuário digitou "abc"), mostre uma mensagem de erro e peça o valor novamente (repita até conseguir um número válido)
- Não aceite valores negativos — se for negativo, avise e peça de novo

**Teste esperado:** digitar "abc", depois "-10", depois "50.5" — o programa só deve aceitar o "50.5" e seguir em frente.

---

## Exercício 4 — Listar gastos

**Objetivo:** implementar a opção "Listar".

**Requisitos:**
- Percorra a lista `gastos` com `for`
- Mostre cada gasto formatado, por exemplo:
  ```
  [1] Mercado - R$150.75 - Alimentação - 2026-09-16
  ```
- Se a lista estiver vazia, mostre uma mensagem avisando (ex: `"Nenhum gasto cadastrado ainda."`)

**Teste esperado:** listar sem nenhum gasto cadastrado (ver o aviso) e depois com 2-3 gastos (ver todos formatados).

---

## Exercício 5 — Editar gasto

**Objetivo:** implementar a opção "Editar".

**Requisitos:**
- Peça o `id` do gasto que o usuário quer editar
- Procure na lista um dicionário com aquele `id`
- Se encontrar, peça os novos valores (descrição, valor, categoria, data) e atualize o dicionário
- Se não encontrar, mostre uma mensagem de erro (ex: `"Gasto não encontrado."`) sem travar o programa
- Reaproveite a validação do Exercício 3 para o novo valor

**Teste esperado:** editar um gasto existente (conferir que mudou ao listar) e tentar editar um `id` que não existe (ver a mensagem de erro).

---

## Exercício 6 — Excluir gasto

**Objetivo:** implementar a opção "Excluir".

**Requisitos:**
- Peça o `id` do gasto a excluir
- Procure e remova o dicionário correspondente da lista
- Se não encontrar, mostre mensagem de erro
- Confirme a exclusão com uma mensagem de sucesso

**Teste esperado:** excluir um gasto e confirmar (via "Listar") que ele sumiu. Tentar excluir um `id` inexistente sem travar.

---

## Exercício 7 — Relatório: total geral

**Objetivo:** implementar a primeira parte da opção "Resumo".

**Requisitos:**
- Percorra a lista `gastos` somando todos os valores em uma variável acumuladora
- Mostre o total formatado (ex: `"Total gasto: R$450.30"`)

**Teste esperado:** o total mostrado deve bater com a soma manual dos gastos cadastrados.

---

## Exercício 8 — Relatório por categoria

**Objetivo:** completar a opção "Resumo" agrupando por categoria.

**Requisitos:**
- Crie um dicionário vazio para acumular os totais por categoria (ex: `totais_categoria = {}`)
- Para cada gasto, se a categoria já existe no dicionário, some o valor; se não existe, crie a chave com o valor
- Ao final, percorra esse dicionário e mostre cada categoria com seu total

**Teste esperado:** cadastrar gastos em pelo menos 2 categorias diferentes e ver os totais certos por categoria no resumo.

---

## Exercício 9 — Salvar em arquivo JSON

**Objetivo:** persistir os dados para não perder ao fechar o programa.

**Requisitos:**
- Importe o módulo `json`
- Crie uma função `salvar_dados()` que escreve a lista `gastos` inteira em um arquivo `gastos.json`
- Chame essa função toda vez que um gasto for adicionado, editado ou excluído

**Teste esperado:** adicionar um gasto e conferir que o arquivo `gastos.json` foi criado/atualizado com o conteúdo certo (pode abrir o arquivo para conferir).

---

## Exercício 10 — Carregar dados ao iniciar

**Objetivo:** ler os dados salvos quando o programa abre.

**Requisitos:**
- Antes do loop do menu, tente carregar o `gastos.json` para dentro da lista `gastos`
- Use `os.path.exists()` (ou `try/except`) para tratar o caso do arquivo ainda não existir (primeira execução) — nesse caso, comece com lista vazia

**Teste esperado:** adicionar gastos, fechar o programa, abrir de novo — os gastos devem continuar lá.

---

## Exercício 11 — Separar em módulos

**Objetivo:** organizar o código em arquivos diferentes.

**Requisitos:**
- Crie os arquivos `arquivo.py` (funções de salvar/carregar), `gastos.py` (funções de adicionar/editar/excluir/listar) e `relatorios.py` (funções de resumo)
- Mova as funções correspondentes para cada arquivo
- No `main.py`, importe as funções necessárias e mantenha só o menu

**Teste esperado:** o programa deve continuar funcionando exatamente igual a antes, só que agora organizado em módulos.

---

Quando terminar um exercício, me mostra o que você fez que eu reviso e explico o que fizer sentido ajustar.
