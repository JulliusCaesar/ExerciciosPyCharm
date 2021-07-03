'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
com a média atingida: - média abaixo de 5,0 REPROVADO. - Média entre 5,0 e 6,9 RECUPERAÇÃO. - Média 7,0 ou maior APROVADO'''
print('\033[33m===\033[m'*15, 'EX040', '\033[33m===\033[m'*15)
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2)/2
if media >= 7:
    print('Sua média foi {:.1f} e você foi APROVADO'.format(media))
elif 5 <= media <= 6.9:
    print('Sua média é {:.1f} e você está de RECUPERAÇÃO!'.format(media))
else:
    print('Sua média é {:.1f} e você foi REPROVADO!'.format(media))
