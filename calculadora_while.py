while True:
    opera = int(input("Digite uma operação:\n 1 - Multiplicação  \n 2 - Divisão \n 3 - Adição \n 4 - Subtração: "))
    if opera == 1:
        nume1=float(input("Digite um número: "))
        nume2=float(input("Digite um número: "))
        mult = nume1*nume2
        print("O resultado da multiplicação de:",nume1,"*",nume2,"é igual a:",mult)
        break
    elif opera == 2:
        nume1=float(input("Digite um número: "))
        nume2=float(input("Digite um número: "))
        div = nume1/nume2
        print("O resultado da divisão de:",nume1,"/",nume2,"é igual a:",div)
        break
    elif opera == 3:
        nume1=float(input("Digite um número: "))
        nume2=float(input("Digite um número: "))
        soma = nume1+nume2
        print("O resultado da soma de:",nume1,"+",nume2,"é igual a:",soma)
        break
    elif opera == 4:
        nume1=float(input("Digite um número: "))
        nume2=float(input("Digite um número: "))
        sub = nume1-nume2
        print("O resultado da subtração de:",nume1,"-",nume2,"é igual a:",sub)
        break
    else:
        print("Programa terminado")
        break
   



