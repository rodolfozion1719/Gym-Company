# 🏋️‍♂️ Gym Companion (Gym Comp)

Software de linha de comando (CLI) em Python desenvolvido para o gerenciamento e acompanhamento de treinos de musculação[cite: 7, 8, 9]. 

O projeto nasceu de uma necessidade real: centralizar o registro dos treinos e substituir anotações manuais dispersas por um sistema próprio, estruturado e evolutivo[cite: 9]. Além do uso pessoal, o **Gym Companion** serve como laboratório prático para aplicar conceitos de Engenharia de Software desde o 1º semestre do Bacharelado em Inteligência Artificial na Universidade Federal de Jataí (UFJ).

---

## ✅ O que já funciona (v0.1 — Versão Atual)

A primeira versão foi construída no 1º semestre utilizando **programação estruturada** em Python, focando na simplicidade e no registro durante a execução do treino[cite: 7]:

- **Divisões de Treino:** Menu interativo organizado por grupos musculares (*Peito/Ombro, Costas/Antebraço, Tríceps/Bíceps, Perna 1 e Perna 2*)[cite: 7].
- **Registro Progressivo:** Acompanhamento dinâmico de exercícios, séries, repetições e cargas utilizadas[cite: 7].
- **Ajuste de Carga entre Séries:** Lógica que permite manter ou alterar o peso apenas enquanto ainda restam séries a serem executadas (`if i < series - 1`)[cite: 7].
- **Resumo do Treino:** Consolidação dos dados da sessão em listas e dicionários na memória ao final do treino[cite: 7].

---

## 💡 Ideias e Roadmap de Evolução

O desenvolvimento segue uma abordagem incremental, evoluindo por etapas conforme novos conceitos técnicos são dominados:

### Fase 1: Refatoração e Persistência (Próximo Passo)
- [ ] **Programação Orientada a Objetos (POO):** Migrar o código procedural para uma arquitetura orientada a objetos, separando responsabilidades nas classes `Treino`, `Exercicio`, `Serie` e `Registro`.
- [ ] **Armazenamento de Dados:** Salvar os treinos inicialmente em arquivos legíveis (`.txt` / `.json`) e evoluir para um banco de dados local com **SQLite**[cite: 5].
- [ ] **Histórico e Flexibilidade:** Permitir pular exercícios durante o treino, definir a quantidade de exercícios do dia e consultar treinos anteriores[cite: 5, 6].

### Fase 2: Métricas e Hábitos de Saúde
- [ ] **Recordes Pessoais (PRs):** Identificação automática de cargas máximas atingidas por exercício[cite: 6].
- [ ] **Cálculo de Volume:** Cálculo preciso do volume de treino ($\text{carga} \times \text{repetições}$) por série, exercício e volume semanal[cite: 6].
- [ ] **Monitoramento Completo:** Incluir contagem diária de **água**, registro de **cárdio (km percorridos)**, cronômetro de descanso entre séries e guia de execução dos exercícios[cite: 6, 9].

### Fase 3: Visualização, Interface e Inteligência Artificial
- [ ] **Estatísticas e Gráficos:** Geração de relatórios visuais de progressão de carga e volume ao longo do tempo[cite: 5, 9].
- [ ] **Interface Gráfica / Mobile:** Evoluir do terminal (CLI) para uma interface visual mais amigável ou aplicativo para celular[cite: 5, 8].
- [ ] **Análise com IA:** Integrar modelos de Inteligência Artificial para analisar a evolução dos treinos, identificar estagnação e sugerir progressões de carga[cite: 6, 9].

---

## 📂 Arquitetura Planejada

Para sustentar o crescimento do projeto nas próximas fases, a estrutura de diretórios foi projetada para separar a interface, as regras de negócio e o banco de dados:

```text
GymCompanion/
│
├── main.py        # Ponto de entrada e fluxo de interação (CLI)
├── models.py      # Classes e regras de negócio (POO)
├── database.py    # Conexão e operações de persistência (SQLite)
├── README.md      # Documentação do projeto
└── data/          # Armazenamento local dos registros
