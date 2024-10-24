num1 = 0
num2 = 0
result = 0
op = " "

while True:
    num1 = float(input("Digite o primero número: "))


    op = input('digita a operação matematica: ')

    num2 = float(input("Digite o segundo número: "))


    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '/':
        result = num1 / num2
    elif op == 'x':
        result = num1 * num2
    else:
        print("Operação não reconhecida!")

    print('{} {} {} = {}'.format(num1, op, num2, result))

