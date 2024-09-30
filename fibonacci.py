def fibonacci(num):
    sequencia = [0, 1]

    while sequencia[-1] < num:
        sequencia.append(sequencia[-1] + sequencia[-2])
        
    if num in sequencia:
        return f"O número {num} pertence à sequência de Fibonacci"
    else:
        return f"O número {num} NÃO pertence à sequência de Fibonacci"

numero = int(input("Informe um número inteiro: "))
print(fibonacci(numero))