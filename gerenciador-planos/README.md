# Desafio: Sistema de Gerenciamento de Planos 

Desenvolver um sistema de gerenciamento de planos telefônicos, onde os usuários podem realizar chamadas com custo baseado na duração e saldo disponível no plano. O sistema deve permitir:

- Criar usuários de plano pré-pago.
- Realizar chamadas deduzindo o saldo do plano.
- Exibir mensagens de sucesso ou erro dependendo da situação.
- Validar entradas para evitar erros como durações inválidas ou saldos negativos.

# Entrada

1. Nome do usuário (string).
2. Número de telefone do usuário (string).
3. Saldo inicial do plano pré-pago (número decimal).
4. Número do destinatário da chamada (string).
5. Duração da chamada em minutos (número inteiro).

# Saída

1. **Mensagem de sucesso:**
   - Quando a chamada é realizada com sucesso, exibe:  
     `"Chamada para <destinatário> realizada. Saldo atual: $<saldo_atual>."`

2. **Mensagem de erro:**
   - Se o saldo for insuficiente:  
     `"Saldo insuficiente para realizar a chamada."`
   - Se a duração da chamada for inválida (menor ou igual a zero):  
     `"Erro: Duração da chamada deve ser maior que zero."`

3. **Erros de validação:**
   - Se o saldo inicial for negativo:  
     `"Erro: O saldo inicial não pode ser negativo."`
   - Se o valor a ser deduzido for maior que o saldo disponível:  
     `"Erro: Valor a deduzir maior que o saldo disponível."`


