import sys


class ModeloIA:
    """Representa um modelo de IA com atributos relevantes para recomendação."""

    def __init__(self, nome, desempenho, velocidade, custo, capacidades):
        self.nome = nome
        self.desempenho = desempenho
        self.velocidade = velocidade
        self.custo = custo
        self.capacidades = capacidades

    def __str__(self):
        return self.nome


def recomendar_modelo(caracteristicas, modelos):
    """
    Recomenda o melhor modelo com base nas características fornecidas.
    """
    modelo_recomendado = None
    capacidades_usuario = [
        capacidade.casefold() for capacidade in caracteristicas["Capacidades"]
    ]

    for modelo in modelos:
        capacidades_modelo = [
            capacidade.casefold() for capacidade in modelo.capacidades
        ]

        # Verifica compatibilidade de capacidades e prioriza os critérios
        if all(capacidade in capacidades_modelo for capacidade in capacidades_usuario):
            if modelo_recomendado is None or (
                modelo.desempenho >= caracteristicas["Desempenho"]
                and modelo.velocidade >= caracteristicas["Velocidade"]
                and modelo.custo <= caracteristicas["Custo"]
            ):
                modelo_recomendado = modelo

    return modelo_recomendado if modelo_recomendado else "Nenhum modelo encontrado."


def gerar_explicacao(modelo, caracteristicas):
    """
    Gera uma explicação detalhada sobre o modelo recomendado.
    """
    if isinstance(modelo, ModeloIA):
        explicacao = (
            f"O {modelo.nome} é o modelo recomendado com base nos seguintes critérios:\n"
            f"- Desempenho mínimo exigido: {caracteristicas['Desempenho']}, fornecido: {modelo.desempenho}\n"
            f"- Velocidade mínima exigida: {caracteristicas['Velocidade']}, fornecida: {modelo.velocidade}\n"
            f"- Custo máximo permitido: {caracteristicas['Custo']}, fornecido: {modelo.custo}\n"
            f"- Capacidades compatíveis: {', '.join(modelo.capacidades)}"
        )
        return explicacao
    else:
        return modelo


def obter_caracteristicas():
    """
    Coleta as características do usuário com validação básica.
    """
    try:
        caracteristicas = {}
        caracteristicas["Desempenho"] = int(
            input("Informe o desempenho mínimo: ").strip()
        )
        caracteristicas["Velocidade"] = int(
            input("Informe a velocidade mínima: ").strip()
        )
        caracteristicas["Custo"] = int(
            input("Informe o custo máximo permitido: ").strip()
        )
        capacidades = (
            input("Informe as capacidades desejadas separadas por vírgula: ")
            .strip()
            .split(",")
        )
        caracteristicas["Capacidades"] = [
            capacidade.strip() for capacidade in capacidades
        ]
        return caracteristicas
    except ValueError:
        print(
            "Erro: certifique-se de fornecer números inteiros válidos para desempenho, velocidade e custo."
        )
        sys.exit(1)


# Lista de modelos disponíveis
modelos = [
    ModeloIA(
        "Claude 3 Sonnet",
        8,
        10,
        6,
        [
            "pesquisa",
            "desenvolvimento acelerado",
            "codificação",
            "recuperação de informações",
        ],
    ),
    ModeloIA(
        "Claude 3 Haiku", 7, 9, 5, ["velocidade", "resumo de dados não estruturados"]
    ),
    ModeloIA("Claude 3 Opus", 9, 10, 5, ["pesquisa", "desenvolvimento acelerado"]),
]

# Execução principal
if __name__ == "__main__":
    caracteristicas_entrada = obter_caracteristicas()
    melhor_modelo = recomendar_modelo(caracteristicas_entrada, modelos)
    explicacao = gerar_explicacao(melhor_modelo, caracteristicas_entrada)
    print(explicacao)
