from analysis import carregar_dados, calculo
from llm import analise_ia


def main():

    # Carrega os dados
    df = carregar_dados("data/cards.csv")

    # Calcula as métricas
    metricas = calculo(df)

    print("\n=== POKÉMON CARD MARKET ANALYST ===\n")

    print(metricas.to_string(index=False))

    pergunta = input(
        "\nTem alguma duvida?: "
    )

    resposta = analise_ia(
        pergunta,
        metricas.to_string(index=False)
    )

    print("\n=== ANÁLISE ===\n")
    print(resposta)


if __name__ == "__main__":
    main()