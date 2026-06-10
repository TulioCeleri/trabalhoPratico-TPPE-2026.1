# Trabalho Prático 1 - TPPE-2026.1

## Autores

* **Pedro Ferreira Gondim - 222026377**
* **Túlio Augusto Celeri - 222026715**
* **Guilherme Evangelista Ferreira dos Santos - 200038028**

---

## Descrição

Este projeto implementa uma solução para **comparação e deduplicação de autores em bases bibliográficas**, utilizando a metodologia **TDD (Test-Driven Development)**.

O desenvolvimento foi realizado de forma incremental, seguindo o ciclo:

1. Escrever um teste que falha (**RED**);
2. Implementar a solução mínima para fazê-lo passar (**GREEN**);
3. Refatorar o código mantendo todos os testes aprovados (**REFACTOR**).

---

## Tecnologias Utilizadas

* Python 3.10+
* Pytest

---

## Estrutura do Projeto

```text
trabalhoPratico-TPPE-2026.1/
│
├── src/
│   ├── __init__.py
│   ├── author_record.py
│   ├── author_deduplicator.py
│   ├── name_normalizer.py
│   └── name_matcher.py
│
├── tests/
│   ├── __init__.py
│   ├── test_case1_typographic.py
│   ├── test_case2_surname_initials.py
│   ├── test_case3_particles.py
│   ├── test_case4_grouped_initials.py
│   └── test_case5_author_ids.py
│
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Instalação

Clone o repositório:

```bash
git clone <url-do-repositorio>
cd trabalhoPratico-TPPE-2026.1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Executando os Testes

Executar todos os testes:

```bash
pytest
```

Executar apenas um caso específico:

```bash
pytest -m caseN
```

Exemplo:

```bash
pytest -m case4
```

Executar os testes com saída detalhada:

```bash
pytest -v
```

---

## Casos de Deduplicação

Os testes são organizados por marcadores do Pytest:

| Marcador | Descrição               |
| -------- | ----------------------- |
| case1    | Diferenças tipográficas |
| case2    | Sobrenome e iniciais    |
| case3    | Partículas opcionais    |
| case4    | Iniciais agrupadas      |
| case5    | Deduplicação de autores |

---

## Funcionalidades Implementadas

### Modelo de Autor

A classe `AuthorRecord` representa um registro contendo:

* Identificador do autor (`author_id`);
* Nome do autor.

---

### Normalização de nomes

A classe `NameNormalizer` realiza:

* Padronização de apóstrofos;
* Remoção de espaços extras;
* Remoção de espaços nas extremidades;
* Padronização de capitalização dos nomes.

---

### Comparação de nomes

A classe `NameMatcher` implementa as regras de equivalência entre autores.

#### Caso 1 - Diferenças tipográficas

Exemplo:

```text
D'Avila == D’Avila
```

---

#### Caso 2 - Sobrenome com iniciais

Permite comparar nomes completos com versões abreviadas.

Exemplos:

```text
Seabra A M == Ana de Mattos Seabra
Souza C. == Cassius de Souza
```

---

#### Caso 3 - Partículas opcionais

Considera opcionais partículas como:

```text
de, da, do, dos, das
```

Exemplos:

```text
Luiz Oliveira Souza == Luiz de Oliveira de Souza
Luiz de O. de Souza == Luiz de Oliveira de Souza
```

---

#### Caso 4 - Iniciais agrupadas

Permite comparar iniciais agrupadas com nomes completos.

Exemplos:

```text
AM Seabra == Ana de Mattos Seabra
SH Guaraldi == Sergio Henrique Guaraldi
VC Junior == Valter Cury Junior
```

---

## Deduplicação de Autores

A classe `AuthorDeduplicator` é responsável por identificar autores equivalentes e eliminar registros duplicados.

Funcionalidades implementadas:

* Identificação de autores equivalentes;
* Remoção de registros duplicados;
* Preservação do menor `author_id`;
* Suporte à deduplicação de listas contendo múltiplos autores.

Exemplo:

Entrada:

```text
(10, AM Seabra)
(5, Ana de Mattos Seabra)
(20, Cassius de Souza)
```

Saída:

```text
(5, Ana de Mattos Seabra)
(20, Cassius de Souza)
```

---

## Metodologia de Desenvolvimento

O projeto foi desenvolvido utilizando **Test-Driven Development (TDD)**.

Cada funcionalidade foi implementada seguindo o fluxo:

1. Criar um teste que falha;
2. Implementar a solução mínima;
3. Refatorar o código preservando o comportamento validado pelos testes.
