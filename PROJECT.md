🐍# PROJECT: GymComp (Gym Companion)

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

4. Divisão de Responsabilidades
models.py: Contém as classes com os dados e cálculos matemáticos. Não utiliza comandos de terminal como input ou print.
database.py: Centraliza as operações no banco SQLite (criar tabelas, inserir treinos e consultar histórico).
main.py: Responsável pela interface com o usuário, exibição de menus e captura de dados pelo teclado.
exercicios.py / treino.py: Armazenam cadastros fixos e rotinas para agilizar o preenchimento.

5. Histórico de Versões
v0.1.0 (Procedural): Primeira versão funcional em script único, com loops e listas simples no terminal.
v0.2.0 (Estruturado): Correção do cálculo de tonelagem por série, fim dos erros de tipo e adição de resumo detalhado por exercício.
v0.3.0 (Orientado a Objetos): Criação das classes Serie, Exercicio e Treino, movendo os cálculos para dentro dos objetos.
v0.4.0 (Persistência): Conexão com banco SQLite para gravar treinos de forma definitiva.

6. Planejamento do Banco de Dados (SQLite)
O banco de dados armazena os treinos em três estruturas conectadas:
Treinos: Guarda o identificador do treino, data de realização, divisão muscular e volume total acumulado.
Exercícios do Treino: Guarda quais exercícios foram executados na sessão, vinculados ao identificador do treino correspondente.
Séries: Guarda o número da série, carga em kg e repetições executadas, vinculadas ao identificador do exercício correspondente.

7. Roadmap
[x] v0.1.0: Entrada de repetições e ajuste dinâmico de carga
[x] v0.2.0: Cálculo exato de volume de treino e relatório final
[ ] v0.3.0: Organização em classes (POO) no models.py
[ ] v0.4.0: Salvamento automático em SQLite (database.py)
[ ] v0.5.0: Comparativo de evolução de carga em relação ao treino passado
[ ] v1.0.0: CLI finalizada com exportação de relatórios
