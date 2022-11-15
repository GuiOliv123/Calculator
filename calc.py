import math

while True:
    firstNum = input("Indique o primeiro numero (Caso pretenda saber a raiz quadrada este numero será ignorado):")
    operator = input("Indique o operador (+ - / * % ^ sqrt):")
    secNum = input("Indique o segundo numero:")
    if firstNum.isnumeric() and secNum.isnumeric():
        if operator == "+":
            print(int(firstNum) + int(secNum))
        elif operator == "-":
            print(int(firstNum) - int(secNum))
        elif operator == "*":
            print(int(firstNum) * int(secNum))
        elif operator == "/":
            if int(secNum) != 0:
                print(int(firstNum) / int(secNum))
            else:
                print("Erro - Divisão por 0")
        elif operator == "%":
            print(int(firstNum) % int(secNum))
        elif operator == "^":
            print(int(firstNum) ** int(secNum))
        elif operator == "sqrt":
            if int(secNum) >= 0:
                print(math.sqrt(int(secNum)))
            else:
                print("Erro - Raiz de numero negativo")
        else:
            print("Digite um operador válido")
    else:
        print("Digite numeros válidos")
