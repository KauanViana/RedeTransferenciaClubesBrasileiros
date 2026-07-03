# Rede de Transferências entre os Clubes Brasileiros

## English

This project was developed as part of an academic assignment whose objective is to apply Graph Theory concepts to the construction and analysis of a network based on a freely chosen topic. Our group chose to study player transfers between clubs in the Brazilian Série A Championship, using these transfers to model a relationship network. Through this analysis, we aim to answer questions such as: Which clubs are involved in the highest number of transfers? Which clubs stand out as the main suppliers of players? Which clubs receive the largest number of players from other teams? In addition to these questions, other structural properties of the network will also be investigated using Graph Theory techniques.

The project is divided into two stages:

1. Data collection and preprocessing
   - Collect transfer data
   - Clean and preprocess the data
   - Generate a CSV file
   - Generate an Excel file
2. Network construction

### Running the Project

```bash
python src/coleta_dados.py
python src/trata_dados.py
```

## Pt-BR
Este projeto foi desenvolvido como parte de um trabalho acadêmico cujo objetivo é aplicar conceitos da Teoria dos Grafos na construção e análise de uma rede baseada em um tema de livre escolha. Nosso grupo optou por estudar as transferências de jogadores entre os clubes da Série A do Campeonato Brasileiro, utilizando essas movimentações para modelar uma rede de relacionamentos. A partir dessa análise, buscamos responder a questões como: quais clubes participam do maior número de transferências? Quais se destacam como principais fornecedores de jogadores? Quais recebem o maior número de atletas provenientes de outros clubes? Além dessas, outras características estruturais da rede também serão investigadas por meio das ferramentas da Teoria dos Grafos.

Projeto separado em 2 etapas:

1. Coleta e tratamento dos dados
    - coletar transferências
    - tratar os dados
    - gerar CSV
    - gerar Excel
2. Criação da Rede

### Executando

```bash
python src/coleta_dados.py
python src/trata_dados.py
```