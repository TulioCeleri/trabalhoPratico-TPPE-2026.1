# Trabalho Pratico 1 - TPPE-2026.1

## Autores

- **Pedro Ferreira Gondim - 222026377**
- **Túlio Augusto Celeri - 222026715**
- **Guilherme Evangelista Ferreira dos Santos - 200038028**

## Descrição

Este projeto implementa uma solução para deduplicação de autores em bases bibliográficas, utilizando a metodologia **TDD (Test-Driven Development)**.

O desenvolvimento é realizado de forma incremental, seguindo o ciclo:

1. Escrever um teste que falha (RED)
2. Implementar o mínimo necessário para fazê-lo passar (GREEN)
3. Refatorar o código mantendo os testes aprovados (REFACTOR)

## Tecnologias Utilizadas

- Python 3.10+
- Pytest

## Estrutura do Projeto

```text
trabalhoPratico-TPPE-2026.1/
│
├── src/
│   ├── author_record.py
│   └── name_normalizer.py
│
├── tests/
│   └── test_case1_typographic.py
│
├── pytest.ini
├── requirements.txt
└── README.md
```

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

## Executando os Testes

Executar todos os testes:

```bash
pytest
```

Executar apenas os testes do Caso N:

```bash
pytest -m caseN
```

Executar testes com saída detalhada:

```bash
pytest -v
```

## Casos de Deduplicação

Os testes são organizados por marcadores do Pytest:

| Marcador | Descrição |
|-----------|-----------|
| case1 | Diferenças tipográficas |
| case2 | Sobrenome e iniciais |
| case3 | Partículas opcionais |
| case4 | Iniciais agrupadas |
| case5 | IDs diferentes para o mesmo autor |


## Funcionalidades Implementadas

### Modelo de Autor

A classe `AuthorRecord` representa um registro de autor contendo:

- ID do autor
- Nome do autor

### Normalização de nomes

A classe `NameNormalizer` realiza:

- Padronização de apóstrofos
- Remoção de espaços extras
- Remoção de espaços nas extremidades
- Padronização de capitalização dos nomes
