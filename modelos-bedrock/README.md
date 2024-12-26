# Recomendação de Modelos Amazon Bedrock

## Descrição

Este programa foi desenvolvido para recomendar modelos da Amazon Bedrock com base no orçamento mensal fornecido pelo usuário. Ele avalia os modelos disponíveis e escolhe o mais adequado considerando o custo e a pontuação de desempenho.

O programa utiliza uma lista pré-definida de modelos, cada um com suas respectivas características de preço mensal e pontuação de desempenho. Caso o orçamento do usuário não seja suficiente para nenhum dos modelos, ele sugere o modelo mais próximo em termos de custo.

## Entrada

O programa solicita ao usuário que insira o orçamento mensal em formato numérico (decimal ou inteiro).

### Exemplos de entradas válidas:
- `600`
- `450.50`

### Requisitos para a entrada:
1. O orçamento deve ser um número válido.
2. Caso o valor seja menor que 250, o programa informará que nenhum modelo pode ser recomendado.

Se o usuário inserir um valor inválido, como texto ou caracteres não numéricos, o programa exibirá uma mensagem de erro e encerrará a execução.

## Saída

O programa retorna a recomendação de um modelo com base no orçamento fornecido, incluindo:
1. **Nome do modelo recomendado**.
2. **Motivo da recomendação**:
   - Melhor desempenho dentro do orçamento.
   - Modelo mais próximo do orçamento, caso nenhum esteja dentro do valor disponível.
   - Mensagem informando que o orçamento é insuficiente.

### Exemplos de saída:

1. **Caso o orçamento permita um modelo com o melhor desempenho**:
