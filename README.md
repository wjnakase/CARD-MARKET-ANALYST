# Card-Market-Analyst

Uma ferramenta em Python que utiliza análise de dados e inteligência artificial para analisar a valorização e o comportamento histórico de preços de cartas seja Pokémon, Yugioh, outros jogos de cartas, apesar de ter sido criado pensando no mercado de pokemon.

O projeto combina Python, Pandas e OpenAI para transformar dados históricos de preços em análises compreensíveis através de perguntas em linguagem natural.

== Objetivo ==

O objetivo do projeto é criar um pequeno analista de mercado de cartas, capaz de responder perguntas como:

Qual carta teve a maior valorização?
Qual carta apresentou maior volatilidade?
Quais cartas estão em queda?
Qual carta teve o melhor desempenho?
Qual foi a variação percentual de determinada carta?

== Como funciona ==

O fluxo principal do projeto é:

Arquivo CSV
    ↓
Pandas
    ↓
Cálculo das métricas
    ↓
Resultados da análise
    ↓
OpenAI

O Python é responsável pelos cálculos dos preços e métricas. A IA recebe os resultados e explica as informações de forma clara.

== Métricas analisadas ==

Atualmente o projeto calcula:

Preço inicial
Preço final
Valorização percentual
Volatilidade dos preços

A valorização é calculada por:

Valorização (%) = ((Preço final - Preço inicial) / Preço inicial) × 100

A volatilidade é estimada a partir do desvio padrão das variações percentuais dos preços.

== Tecnologias ==
Python
Pandas
OpenAI API
python-dotenv
CSV
Git/GitHub

