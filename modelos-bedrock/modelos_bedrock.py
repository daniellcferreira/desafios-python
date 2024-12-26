# Lista de dicionários representando os três modelos do Amazon Bedrock
modelos_disponiveis = [
    {"nome": "Claude 3 Opus", "pontuacao_desempenho": 9, "preco_mensal": 600},
    {"nome": "Claude 3 Sonnet", "pontuacao_desempenho": 8, "preco_mensal": 450},
    {"nome": "Claude 3 Haiku", "pontuacao_desempenho": 7, "preco_mensal": 350},
]


# Função para recomendar o modelo com base no orçamento
def recomendar_modelo(modelos, orcamento):
    """
    Recomenda o melhor modelo com base no orçamento fornecido.

    :param modelos: Lista de modelos disponíveis.
    :param orcamento: Orçamento fornecido pelo usuário.
    :return: Nome do modelo recomendado e motivo.
    """
    if orcamento < 250:
        return (
            None,
            "Seu orçamento de R$ {:.2f} é muito baixo para recomendar um modelo adequado.".format(
                orcamento
            ),
        )

    modelos_dentro_orcamento = [
        modelo for modelo in modelos if modelo["preco_mensal"] <= orcamento
    ]

    if not modelos_dentro_orcamento:
        modelo_mais_proximo = min(
            modelos, key=lambda x: abs(x["preco_mensal"] - orcamento)
        )
        return (
            modelo_mais_proximo["nome"],
            "Nenhum modelo está dentro do orçamento de R$ {:.2f}. O modelo mais próximo custa R$ {:.2f}.".format(
                orcamento, modelo_mais_proximo["preco_mensal"]
            ),
        )

    melhor_modelo = max(
        modelos_dentro_orcamento, key=lambda x: x["pontuacao_desempenho"]
    )
    return (
        melhor_modelo["nome"],
        "Recomendado por melhor desempenho dentro do orçamento de R$ {:.2f}.".format(
            orcamento
        ),
    )


# Solicitar orçamento ao usuário
try:
    orcamento_usuario = float(
        input("Por favor, insira seu orçamento mensal (em R$): ").strip()
    )
except ValueError:
    print("Erro: Por favor, insira um valor numérico válido para o orçamento.")
    exit(1)

# Chamada da função para recomendar o modelo
modelo_recomendado, motivo = recomendar_modelo(modelos_disponiveis, orcamento_usuario)

# Exibir a recomendação
if modelo_recomendado:
    print(f"Modelo recomendado: {modelo_recomendado}. {motivo}")
else:
    print(motivo)
