""" Nome: Matheus Bezerra Domingos
    Data: 20/11/2024
    Objetivo: "Usando if, else, elseif"
"""
qnt2 = 0
qnt = float(input("Digite um numero..: "))

if qnt >= 10:
    print("É maior que dez")
else:
    print("É menor que dez")


#qnt2 = float(input("Digite um numero..: "))

while qnt2 <= 100:
    qnt2 = float(input("Digite um numero..: "))

    if qnt2 <= 10:
      print("É menor que 50")
    elif qnt2 <= 99: #o famoso else if
       print("É menor que 99")
    else:
      print("É maior ou igual a cem, fim do loop")