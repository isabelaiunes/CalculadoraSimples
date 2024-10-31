print("\n******************* Calculadora em Python *******************")
print("\nSelecione o número da operação desejada")
print("1 - Soma")
2- Subtração, 3- Multiplicação, 4- Divisão")
operacao = (input('Qual operação você quer fazer? '))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if operacao == "1":
    resultado = num1 + num2
    print("O resultado é: ", resultado)
elif operacao == "2":
    resultado = num1 - num2
    print("O resultado é: ", resultado)
elif operacao == "3":
    resultado = num1 * num2
    print("O resultado é: ", resultado)
elif operacao == "4":
    if num2 == 0:  # Verifica se o divisor é zero
        print("Número não divisível por zero.")
    else:
        resultado = num1 % num2
else:
    print('Operação Inválida. Selecione um dos números acima.')