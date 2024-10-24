print ("Bem-vindo a Calculadora!")
num1 = float(input( "Insira o primeiro número: " ))
num2 = float(input( "Insira o segundo número "))
operação = input( "Selecione uma operação (+, -, *, /): ")
if operação == "+":
    resultado = num1 + num2
    print("O resultado é: ", resultado)
elif operação == "-":
    resultado = num1 - num2
    print("O resultado é: ", resultado)
elif operação == "*":
    resultado = num1 * num2
    print("O resultado é: ", resultado)
elif operação == "/":
    resultado = num1 / num2
    print("O resultado é: ", resultado)
else:
    print("Operação Inválida.")
