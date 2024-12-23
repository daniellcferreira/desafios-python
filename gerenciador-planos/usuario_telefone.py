class UsuarioTelefone:
    """Classe base para representar um usuário de telefone."""

    def __init__(self, nome, numero, plano):
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano

    def fazer_chamada(self, destinatario, duracao):
        """Realiza uma chamada, deduzindo o custo do saldo do plano."""
        if duracao <= 0:
            return "Erro: Duração da chamada deve ser maior que zero."

        custo = self.__plano.custo_chamada(duracao)

        if self.__plano.verificar_saldo() >= custo:
            self.__plano.deduzir_saldo(custo)
            return f"Chamada para {destinatario} realizada. Saldo atual: ${self.__plano.verificar_saldo():.2f}"
        return "Saldo insuficiente para realizar a chamada."


class Plano:
    """Classe base para representar um plano de telefone."""

    def __init__(self, saldo_inicial):
        if saldo_inicial < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")
        self.__saldo = saldo_inicial

    def verificar_saldo(self):
        """Retorna o saldo atual."""
        return self.__saldo

    def custo_chamada(self, duracao):
        """Calcula o custo de uma chamada com base na duração."""
        return duracao * 0.10  # Custo fixo por minuto.

    def deduzir_saldo(self, valor):
        """Deduz o valor do saldo."""
        if valor > self.__saldo:
            raise ValueError("Valor a deduzir maior que o saldo disponível.")
        self.__saldo -= valor


class UsuarioPrePago(UsuarioTelefone):
    """Classe para representar um usuário de plano pré-pago."""

    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


def main():
    """Função principal para execução do programa."""
    try:
        nome = input("Digite o nome do usuário: ")
        numero = input("Digite o número do telefone: ")
        saldo_inicial = float(input("Digite o saldo inicial do plano: "))

        usuario = UsuarioPrePago(nome, numero, saldo_inicial)

        destinatario = input("Digite o número do destinatário: ")
        duracao = int(input("Digite a duração da chamada (em minutos): "))

        resultado = usuario.fazer_chamada(destinatario, duracao)
        print(resultado)

    except ValueError as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()
