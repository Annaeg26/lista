'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''

n1 = int(input('insira o número inteiro'))
n2 = int(input('Insira o número inteiro'))
n3 = float(input('insira o número real'))

c1 = (n1 * 2) + (n2/2)
c2 = (n1 * 3) + n3
c3 = n3**3

print(f'o produto do dobro do primeiro {n1} com metade do segundo {n2}  é -- {c1}')
print(f'a soma do triplo do primeiro {n1} com o terceiro {n3}. {c2}')
print(f'o terceiro {n3} elevado ao cubo {c3}')