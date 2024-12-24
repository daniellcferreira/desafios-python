import sys

# Dicionário associando características normalizadas aos modelos Claude 3
caracteristicas_modelos = {
    "automatizar tarefas": "Claude 3 Opus",
    "pesquisa e desenvolvimento": "Claude 3 Opus",
    "resposta rápida e capacidade de resposta quase instantânea": "Claude 3 Haiku",
    "motores de chatbots de lojas": "Claude 3 Haiku",
    "moderação de conteúdo": "Claude 3 Haiku",
    "processamento de tarefas mais básicas": "Claude 3 Haiku",
    "raciocínio cuidadoso": "Claude 3 Sonnet",
    "processamento de dados": "Claude 3 Sonnet",
    "aplicações de vendas": "Claude 3 Sonnet",
    "extração de texto de imagens": "Claude 3 Sonnet",
    "equilíbrio ideal entre inteligência e velocidade": "Claude 3 Sonnet",
}

# Normalizar o dicionário para facilitar comparações
caracteristicas_modelos = {
    key.lower(): value for key, value in caracteristicas_modelos.items()
}


# Função para encontrar o modelo correspondente à característica fornecida
def encontrar_modelo(caracteristica_fornecida):
    # Buscar diretamente no dicionário normalizado
    return caracteristicas_modelos.get(
        caracteristica_fornecida.lower(), "Modelo não encontrado."
    )


# Função principal para execução
def main():
    print("Bem-vindo ao Identificador de Modelos Claude 3!")
    print("Digite uma característica para encontrar o modelo correspondente.")
    print(
        "Exemplo de características: 'automatizar tarefas', 'raciocínio cuidadoso', ou 'moderação de conteúdo'."
    )
    print("Digite 'sair' para encerrar o programa.\n")

    while True:
        # Solicita entrada do usuário
        caracteristica_fornecida = input("Forneça uma característica: ").strip()

        # Verifica se o usuário deseja sair
        if caracteristica_fornecida.lower() == "sair":
            print("Encerrando o programa. Até logo!")
            break

        # Valida se a entrada não está vazia
        if not caracteristica_fornecida:
            print("Por favor, forneça uma característica válida.\n")
            continue

        # Encontra e exibe o modelo correspondente
        modelo_correspondente = encontrar_modelo(caracteristica_fornecida)
        print(f"Resultado: {modelo_correspondente}\n")


# Invocar a função principal
if __name__ == "__main__":
    main()
