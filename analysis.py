import pandas as pd


def carregar_dados(caminho):
    df = pd.read_csv(caminho)

    df["date"] = pd.to_datetime(df["date"])

    return df


def calculo(df):

    df = df.sort_values(["name", "date"])

    resultados = []

    for nome, grupo in df.groupby("name"):

        primeiro_preco = grupo.iloc[0]["price"]
        ultimo_preco = grupo.iloc[-1]["price"]

        valorizacao = (
            (ultimo_preco - primeiro_preco)
            / primeiro_preco
        ) * 100

        retornos = grupo["price"].pct_change().dropna()

        volatilidade = retornos.std() * 100

        resultados.append({
            "name": nome,
            "initial_price": primeiro_preco,
            "final_price": ultimo_preco,
            "return_percent": valorizacao,
            "volatility_percent": volatilidade
        })

    return pd.DataFrame(resultados)