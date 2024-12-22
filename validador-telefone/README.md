# Desafio: Validação de Número de Telefone

## Objetivo
Imagine que você trabalha para uma empresa de telecomunicações e é responsável por validar se um número de telefone fornecido pelo cliente está no formato correto. Para garantir a precisão dos registros, é essencial que os números de telefone estejam no formato padrão. 

Desenvolva uma função que valide se um número de telefone tem o formato correto conforme o padrão especificado.

---

## Formato Esperado
O formato aceito para números de telefone é: **(XX) 9XXXX-XXXX**, onde:
- `XX` representa dois dígitos de 0 a 9 (código de área).
- `9XXXX-XXXX` representa um número de telefone celular, onde `X` é um dígito de 0 a 9.

### Exemplo de formato correto:
- (11) 91234-5678
- (21) 99876-5432

### Exemplo de formato incorreto:
- (11) 912345678
- (21) 123-4567

---

## Requisitos

### Entrada
- Uma **string** representando o número de telefone.

### Saída
- A saída deve ser uma **mensagem** indicando se o número de telefone é válido ou inválido.

---

