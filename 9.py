'''Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).'''

f = int (input('Digite a temperatura em Farenheit'))
C = (5 * (f-32) / 9)

print(f'Valor em Celsius é: {C:.2F}')