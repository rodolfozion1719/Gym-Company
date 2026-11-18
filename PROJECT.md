#🐍 PROJECT: GymComp (Gym Companion)

Documento técnico com diretrizes, regras de negócio, arquitetura e planejamento do projeto.

---

## 1. Visão Geral

O **GymComp** é um software em Python desenvolvido para registro e análise de treinos de musculação direto pelo terminal (CLI). O foco principal é viabilizar o acompanhamento prático da **sobrecarga progressiva** (*progressive overload*), permitindo anotar séries, repetições e alterações de carga sem atrito.

O projeto documenta a evolução da estrutura do código, saindo de um script procedural básico para uma arquitetura orientada a objetos (POO) com persistência em banco de dados relacional.

---

## 2. Regras de Negócio e Métricas

### Entidades do Treino
* **Série:** Unidade básica que guarda o peso utilizado (em kg) e a quantidade de repetições concluídas.
* **Exercício:** Agrupamento de séries pertencentes a um movimento específico (exemplo: Supino Reto, Agachamento).
* **Treino:** Sessão completa com todos os exercícios realizados em uma data, agrupados sob uma divisão (Push, Pull, Legs, etc.).

### Cálculo de Volume (Tonelagem)
O volume total não utiliza médias ou multiplicação simples de listas. O cálculo é feito somando individualmente o esforço de cada série realizada:

* **Volume da série** = Carga (kg) * Repetições
* **Volume do exercício** = Soma do volume de todas as séries daquele exercício
* **Volume da sessão** = Soma do volume de todos os exercícios do treino

### Ajuste de Carga
* O sistema solicita a carga inicial na primeira série.
* Nas séries seguintes, o usuário pode manter o peso anterior ou digitar um novo valor. Isso permite registrar treinos com carga fixa, pirâmide crescente ou drop sets.

---

## 3. Estrutura de Arquivos

```text
Gym-Company/
├── data/              # Pasta reservada para banco de dados local
├── models.py          # Classes do domínio (Serie, Exercicio, Treino)
├── database.py        # Funções de salvamento e leitura no SQLite
├── exercicios.py      # Lista padrão de exercícios por grupo muscular
├── treino.py          # Rotinas prontas e divisões de treino
├── main.py            # Menu principal e fluxo no terminal
│
├── CHANGELOG.md       # Histórico de alterações por versão
├── IDEIAS.md          # Anotações e ideias futuras
├── PROJECT.md         # Documento técnico da arquitetura
└── README.md          # Apresentação do projeto no GitHub
```



## 4. Divisão de Responsabilidades

- **`models.py`:** Contém as classes de domínio (`Serie`, `Exercicio`, `Treino`) com seus atributos e métodos de cálculo matemático interno. Não executa chamadas de interface como `input()` ou `print()`.
- **`database.py`:** Centraliza a camada de persistência com SQLite, isolando comandos de criação de tabelas, inserção de registros e consultas de histórico.
- **`main.py`:** Ponto de entrada do sistema. Gerencia a interface de linha de comando (CLI), menus de navegação, captura de entradas do usuário e formatação dos relatórios na tela.
- **`exercicios.py` / `treino.py`:** Armazenam o catálogo padrão de exercícios por grupo muscular e rotinas pré-montadas para agilizar a seleção durante o treino.

---

## 5. Histórico de Versões

- **`v0.1.0` (Procedural):** Primeira versão funcional desenvolvida como script único, utilizando variáveis em escopo aberto, loops simples e listas paralelas para registrar repetições e cargas.
- **`v0.2.0` (Estruturado):** Correção do cálculo de volume por série, eliminação de erros de tipo (`TypeError`) e introdução de resumo consolidado por exercício ao fim de cada bloco.
- **`v0.3.0` (Orientado a Objetos):** Implementação das classes `Serie`, `Exercicio` e `Treino`, encapsulando as regras de cálculo dentro dos próprios objetos e desacoplando a lógica da interface.
- **`v0.4.0` (Persistência):** Integração com banco de dados relacional SQLite para gravação definitiva de sessões e consulta de treinos passados.

---

## 6. Especificações Técnicas

- **Linguagem:** Python 3.8 ou superior
- **Paradigma:** Programação Orientada a Objetos (POO) com arquitetura modular
- **Dependências Externas:** Nenhuma (utilização exclusiva da biblioteca padrão do Python: `sqlite3`, `math`, `datetime`)
- **Controle de Versão:** Git e repositório remoto no GitHub com fluxo baseado na branch `main`

---

## 7. Planejamento do Banco de Dados (SQLite)

O armazenamento persistente organiza os dados de treino em três entidades relacionais conectadas:

- **Sessões de Treino:** Armazena o identificador único da sessão, data e hora de realização, divisão muscular (`Push`, `Pull`, `Legs`, etc.) e tonelagem total acumulada.
- **Exercícios Executados:** Registra os movimentos realizados em cada sessão, mantendo vínculo com a sessão correspondente e guardando o volume total do exercício.
- **Séries Realizadas:** Registra a ordem de cada série, carga em kg e quantidade de repetições concluídas, vinculadas diretamente ao exercício ao qual pertencem.

---

## 8. Estrutura das Tabelas

- **Tabela `treinos`**
  - `id`: Chave primária (inteiro com incremento automático)
  - `data`: Data e hora da sessão (texto em formato ISO 8601)
  - `divisao`: Nome da divisão muscular trabalhada (texto)
  - `volume_total`: Tonelagem acumulada da sessão inteira (número decimal)

- **Tabela `exercicios_treino`**
  - `id`: Chave primária (inteiro com incremento automático)
  - `treino_id`: Chave estrangeira referenciando `treinos(id)`
  - `nome`: Nome do exercício executado (texto)
  - `volume`: Tonelagem acumulada no exercício (número decimal)

- **Tabela `series`**
  - `id`: Chave primária (inteiro com incremento automático)
  - `exercicio_treino_id`: Chave estrangeira referenciando `exercicios_treino(id)`
  - `numero_serie`: Índice sequencial da série no exercício (número inteiro)
  - `carga`: Peso levantado em kg (número decimal)
  - `repeticoes`: Quantidade de repetições completadas (número inteiro)

---

## 9. Roadmap

- [x] **v0.1.0:** Registro procedural de repetições e ajuste dinâmico de carga entre séries
- [x] **v0.2.0:** Correção matemática do cálculo de volume total e exibição de relatório final
- [ ] **v0.3.0:** Refatoração completa para POO centralizada em `models.py`
- [ ] **v0.4.0:** Gravação automática de treinos em banco SQLite local via `database.py`
- [ ] **v0.5.0:** Consulta comparativa de progressão de carga em relação à sessão anterior do mesmo movimento
- [ ] **v1.0.0:** CLI finalizada e polida, com suporte à exportação de relatórios em Markdown e CSV

[ ] v0.5.0: Comparativo de evolução de carga em relação ao treino passado

[ ] v1.0.0: CLI finalizada com exportação de relatórios
