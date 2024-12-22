import re


def validate_numero_telefone(phone_number):
    """
    Função para validar se um número de telefone está no formato correto: (XX) 9XXXX-XXXX.

    Parâmetros:
        phone_number (str): Número de telefone a ser validado.

    Retorna:
        str: Mensagem indicando se o número de telefone é válido ou inválido.
    """
    # Definindo o padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX
    pattern = r"^\(\d{2}\) 9\d{4}-\d{4}$"

    # Verifica se o padrão definido corresponde ao número de telefone fornecido
    if re.match(pattern, phone_number):
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."


def format_telefone(phone_number):
    """
    Função para formatar o número de telefone no formato correto: (XX) 9XXXX-XXXX.

    Parâmetros:
        phone_number (str): Número de telefone sem formatação (apenas números).

    Retorna:
        str: Número de telefone formatado no padrão (XX) 9XXXX-XXXX.
    """
    # Remover tudo que não for número
    phone_number = re.sub(r"\D", "", phone_number)

    # Verificar se o número tem exatamente 11 dígitos
    if len(phone_number) == 11:
        return f"({phone_number[:2]}) {phone_number[2]}{phone_number[3:7]}-{phone_number[7:]}"
    else:
        return None


# Solicita ao usuário que insira um número de telefone
phone_number = input(
    "Digite o número de telefone no formato (XX) 9XXXX-XXXX ou apenas os números: "
).strip()

# Tenta formatar o número caso tenha sido inserido sem formatação
formatted_number = format_telefone(phone_number)

if formatted_number:
    # Chama a função 'validate_numero_telefone()' com o número de telefone formatado
    result = validate_numero_telefone(formatted_number)
else:
    result = "Número de telefone inválido. O número deve ter 11 dígitos."

# Imprime o resultado
print(result)
