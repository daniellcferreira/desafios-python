# Sistema de Recomendação de Modelos de IA

## Descrição
Este projeto implementa um sistema para recomendar o modelo de inteligência artificial (IA) mais adequado com base em critérios fornecidos pelo usuário. O sistema considera os seguintes atributos para a recomendação:

- **Desempenho**: Avalia o nível de desempenho mínimo exigido.
- **Velocidade**: Determina a velocidade mínima desejada.
- **Custo**: Define o custo máximo permitido para o modelo.
- **Capacidades**: Lista as funcionalidades que o modelo deve oferecer.

Com base nessas entradas, o sistema seleciona o modelo que melhor atende aos critérios fornecidos, priorizando compatibilidade e eficiência.

### Funcionalidades
- Filtragem de modelos com base em capacidades específicas.
- Avaliação de critérios mínimos de desempenho, velocidade e custo.
- Geração de explicação detalhada para o modelo recomendado.

## Entrada
As entradas do sistema são fornecidas pelo usuário e incluem:

1. **Desempenho (int)**: Valor numérico que representa o desempenho mínimo exigido pelo usuário.
2. **Velocidade (int)**: Valor numérico que indica a velocidade mínima desejada.
3. **Custo (int)**: Valor numérico que especifica o custo máximo aceitável.
4. **Capacidades (lista de strings)**: Lista de capacidades desejadas, separadas por vírgulas.

### Formato de Entrada
O sistema solicita os valores na seguinte ordem:

- `Desempenho`: Exemplo: `8`
- `Velocidade`: Exemplo: `10`
- `Custo`: Exemplo: `6`
- `Capacidades`: Exemplo: `pesquisa, codificação`

Exemplo completo de entrada no terminal:
```plaintext
Informe o desempenho mínimo: 8
Informe a velocidade mínima: 10
Informe o custo máximo permitido: 6
Informe as capacidades desejadas separadas por vírgula: pesquisa, codificação
```

## Saída
O sistema retorna uma explicação detalhada sobre o modelo recomendado ou informa que nenhum modelo compatível foi encontrado.

### Exemplos de Saída
1. Caso um modelo seja recomendado:
```plaintext
O Claude 3 Sonnet é o modelo recomendado com base nos seguintes critérios:
- Desempenho mínimo exigido: 8, fornecido: 8
- Velocidade mínima exigida: 10, fornecida: 10
- Custo máximo permitido: 6, fornecido: 6
- Capacidades compatíveis: pesquisa, desenvolvimento acelerado, codificação, recuperação de informações
```

2. Caso nenhum modelo seja encontrado:
```plaintext
Nenhum modelo encontrado.
```

## Como Executar
1. Certifique-se de ter o Python instalado em sua máquina.
2. Execute o script com o seguinte comando:
   ```bash
   python nome_do_arquivo.py
   ```
3. Insira os valores solicitados no terminal.

## Estrutura do Código
1. **Classe ModeloIA**: Representa os modelos de IA disponíveis.
2. **Função recomendar_modelo**: Avalia os modelos disponíveis com base nas entradas do usuário.
3. **Função gerar_explicacao**: Gera uma explicação detalhada sobre o modelo recomendado.
4. **Função obter_caracteristicas**: Coleta e valida as características fornecidas pelo usuário.

---
Este projeto foi desenvolvido para ajudar na seleção eficiente de modelos de IA com base em critérios personalizados. Modifique ou expanda o código conforme necessário para atender às suas necessidades específicas.

