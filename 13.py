'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

h = float(input('insira sua altura'))
s = input('insira seu sexo [f/m] ==>')

if s=='f':
    p=(62.1*h) - 44.7
    print(f'seu peso ideal é {p:.2f}')

else:
    p= (72.7*h) - 58
    print(f'seu peso idela é {p:.2f}')