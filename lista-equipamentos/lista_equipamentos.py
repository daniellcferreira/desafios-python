def coletar_equipamentos():
    """
    Solicita ao usuário que insira uma lista de equipamentos.

    Retorna:
        list: Lista contendo os nomes dos equipamentos informados.
    """
    itens = []
    print("Digite os nomes dos equipamentos. Digite 'sair' para finalizar:")

    while True:
        item = input("Nome do equipamento: ").strip()

        # Verifica se o usuário deseja encerrar
        if item.lower() == "sair":
            break

        # Verifica se a entrada não está vazia
        if item:
            itens.append(item)
        else:
            print("O nome do equipamento não pode ser vazio. Tente novamente.")

    return itens


def exibir_equipamentos(itens):
    """
    Exibe a lista de equipamentos cadastrados.

    Parâmetros:
        itens (list): Lista de equipamentos a serem exibidos.
    """
    if itens:
        print("\nLista de Equipamentos:")
        for item in itens:
            print(f"- {item}")
    else:
        print("\nNenhum equipamento foi cadastrado.")


def main():
    """
    Função principal do programa. Coleta e exibe a lista de equipamentos.
    """
    itens = coletar_equipamentos()
    exibir_equipamentos(itens)


if __name__ == "__main__":
    main()
