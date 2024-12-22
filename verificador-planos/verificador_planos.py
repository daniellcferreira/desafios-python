# Constantes para os limites de consumo e nomes dos planos
LIMITE_ESSENCIAL = 10
LIMITE_PRATA = 20
PLANO_ESSENCIAL = "Plano Essencial Fibra - 50Mbps"
PLANO_PRATA = "Plano Prata Fibra - 100Mbps"
PLANO_PREMIUM = "Plano Premium Fibra - 300Mbps"


def recomendar_plano(consumo):
    """
    Recomenda um plano de internet com base no consumo médio mensal de dados.

    Parâmetros:
        consumo (float): Consumo médio mensal de dados em GB.

    Retorna:
        str: Nome do plano de internet recomendado.
    """
    if consumo <= LIMITE_ESSENCIAL:
        return PLANO_ESSENCIAL
    elif consumo <= LIMITE_PRATA:
        return PLANO_PRATA
    else:
        return PLANO_PREMIUM


def main():
    """
    Função principal do programa. Solicita ao usuário o consumo médio mensal,
    chama a função recomendar_plano e exibe o plano de internet recomendado.

    Fluxo:
        1. Recebe o consumo médio mensal de dados como entrada.
        2. Valida a entrada do usuário.
        3. Calcula o plano recomendado com base no consumo.
        4. Exibe o plano ao usuário.
    """
    try:
        consumo = float(input("Informe o consumo médio mensal de dados (em GB): "))
        if consumo < 0:
            print("O consumo não pode ser negativo. Tente novamente.")
        else:
            print(recomendar_plano(consumo))
    except ValueError:
        print("Entrada inválida! Por favor, insira um número válido.")


if __name__ == "__main__":
    main()
