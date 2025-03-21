
while True:
    nota1 = float(input('Digite a nota do primeiro bimestre: '))
    if (nota1 <= 10) and (nota1 >= 0):
        break

while True:
    nota2 = float(input('Digite a nota do segundo bimestre: '))
    if (nota1 <= 10) and (nota1 >= 0):
        break

while True:
    nota3 = float(input('Digite a nota do terceiro bimestre: '))
    if (nota1 <= 10) and (nota1 >= 0):
        break

while True:
    nota4 = float(input('Digite a nota do quarto bimestre: '))
    if (nota1 <= 10) and (nota1 >= 0):
        break



#o input sempre retorna uma string. Portanto usamos os comando int(numero inteiro) e Float (numero quebrados), na frente do input.

notaTotal = nota1 + nota2 + nota3 + nota4
mediaFinal = notaTotal / 4

print('Nota Total: ',notaTotal)
print(f'Sua média é {mediaFinal:,.2f}')

#Para n precisar colocar a variavel fora da aspas, use (f'{}')
#Se você quiser só mostrar a media direto, pode usar apenas uma variavel, com regra de matematica:
#mediaFinal = (nota1 + nota2 + nota3 + nota4) / 4

if (mediaFinal >= 5 ):
    print('Aluno A P R O V A D O !!!')

elif (mediaFinal >= 3):
    print('Aluno em RECUPERAÇÃO!!!')

else:
    print('Aluno R E P R O V A D O !!!')

print('Fim do ano letivo')



