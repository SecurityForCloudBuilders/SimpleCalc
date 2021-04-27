def calculator(x,operation,y):
    if operation == "+":
        return x+y
    elif operation == "-":
        return x-y
    elif operation == "*":
        return x*y
    elif operation == "/":
        return x*y

if __name__=="__main__":
    while True:
        linha = input("digite> ")
        try:
            x,op,y = linha.split(" ")
            result = calculator(int(x), op ,int(y))
            print(result)
        except ValueError:
            print("Não esqueça dos espaços entre operadores e operandos")

