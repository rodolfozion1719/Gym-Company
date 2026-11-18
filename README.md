# 🏋️‍♂️ GymComp (Gym Companion)

> CLI leve e intuitiva em Python desenvolvida para rastreamento de carga, contagem de repetições e cálculo de volume total em treinos de musculação.

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-orange.svg)
![Version](https://img.shields.io/badge/versão-v0.2.0-brightgreen.svg)

---

## 📌 Sobre o Projeto

O **GymComp** nasceu como uma ferramenta estruturada para resolver um problema real na rotina de academia: registrar de forma rápida e sem distrações cada série, repetição e ajuste de peso executado, calculando a tonelagem acumulada para orientar a progressão de carga.

O projeto documenta a evolução prática desde scripts procedurais em terminal até a modelagem orientada a objetos (POO) e arquitetura modular de software.

---

## 🚀 Funcionalidades Atuais (v0.2.0)

- [x] **Registro Dinâmico de Exercícios:** Inserção e iteração pelas séries planejadas para cada exercício do dia.
- [x] **Ajuste de Cargas entre Séries:** Opção de manter ou recalcular o peso a cada série concluída (suporte a pirâmide crescente, decrescente ou carga fixa).
- [x] **Cálculo Preciso de Volume (Tonelagem):** Soma matemática direta de $(\text{Carga} \times \text{Repetições})$ de cada série individual, sem distorções de médias.
- [x] **Resumo Imediato por Exercício:** Exibição detalhada das cargas utilizadas, repetições batidas e volume levantado logo após o término do movimento.
- [x] **Relatório Final da Sessão:** Visão consolidada de todos os exercícios registrados no treino.

---

## 💻 Exemplo de Execução

```text
===========================
REGISTRO DO TREINO
===========================

Exercício: Supino Reto
Quantas séries ? 3
Carga inicial (kg): 60

Série 1
Carga atual: 60.0 kg
Repetições: 10
Manter a mesma carga? (s/n): s

Série 2
Carga atual: 60.0 kg
Repetições: 10
Manter a mesma carga? (s/n): n
Nova carga: 64

Série 3
Carga atual: 64.0 kg
Repetições: 8

============ Exercício Registrado ============
Exercício: Supino Reto
Cargas: [60.0, 60.0, 64.0]
Repetições: [10, 10, 8]
Séries totais: 3
Volume total levantado: 1712.0 kg
