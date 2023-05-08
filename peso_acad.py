codegordo = 0
codemagro = 0
codealto = 0
codebaixo = 0
pesomgordo = 0
pesommagro = 1000
altalto = 0
altbaixo = 500
somapeso = 0
somalt = 0
qtdc = 0
while True:
    cod = int(input("Informe o código do cliente: "))
    if cod == 0:
        print("Código inválido")
        break
    qtdc += 1
    alt = float(input("Diga a altura do cliente: "))
    peso = float(input("Qual o peso do cliente: "))
    somapeso += peso
    somalt += alt
    if alt > altalto:
        altalto = alt
        codealto = cod
    if alt < altbaixo:
        altbaixo = alt
        codebaixo = cod
    if peso > pesommagro:
        pesommagro = peso
        codemagro = cod
    if peso < pesomgordo:
        pesomgordo = peso
        codegordo = cod
medalt = somalt / qtdc
mpeso = somapeso / qtdc
print("O cliente mais alto é o que tem o código:",codealto,
"\nO cliente mais baixo é o que tem o código:",codebaixo,
"\nO cliente com maior massa corporal é o com o código:",codegordo,
"\nO cliente com a menor massa corporal é o com o código:",codemagro,
"\nA média das alturas foi:",medalt,
"\nA média dos pesos foi:",mpeso)

