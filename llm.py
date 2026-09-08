from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

cliente = OpenAI()


def analise_ia(pergunta, dados):

    prompt = f"""
Você é um analista do mercado de cartas Pokémon. Analise os dados abaixo.

DADOS:
{dados}

PERGUNTA DO USUÁRIO:
{pergunta}

Responda em português.

Utilize somente os dados fornecidos.
Não invente preços ou informações.

Explique de maneira clara como chegou à conclusão.
"""

    resposta = cliente.responses.create(
        model="gpt-5",
        input=prompt
    )

    return resposta.output_text