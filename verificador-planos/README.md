# Desafio: Recomendação de Planos de Internet

## Objetivo
Uma empresa de telecomunicações deseja criar uma solução algorítmica que ajude seus clientes a escolherem o plano de internet ideal com base em seu consumo mensal de dados.

O desafio consiste em implementar uma função chamada `recomendar_plano`, que recebe o consumo médio mensal de dados do cliente como entrada e retorna o plano mais adequado, utilizando estruturas condicionais para a verificação.

---

## Planos Oferecidos
Os planos disponíveis e seus respectivos critérios são:

- **Plano Essencial Fibra - 50Mbps**  
  Recomendado para um consumo médio de até **10 GB**.

- **Plano Prata Fibra - 100Mbps**  
  Recomendado para um consumo médio acima de **10 GB** até **20 GB**.

- **Plano Premium Fibra - 300Mbps**  
  Recomendado para um consumo médio acima de **20 GB**.

---

## Requisitos

### Entrada
- Solicitar ao usuário o consumo médio mensal de dados em **GB** (float).

### Saída
- Retornar o plano de internet ideal para o cliente com base no consumo informado.

