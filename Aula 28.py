from datetime import date
anonasc = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = int(atual - anonasc)
if idade <=9 and idade > 0:
    print('O atetla tem \033[33m{}\033[m anos\nE compete na grade \033[30;44mMIRIM!!\033[m'.format(idade))
elif idade > 9 and idade <= 14:
    print('O atetla tem \033[33m{}\033[m anos\nE compete na grade \033[30;44mINFANTIL!!\033[m'.format(idade))
elif idade > 14 and idade <= 19:
    print('O atetla tem \033[33m{}\033[m anos\nE compete na grade \033[30;44mJUNIOR!!\033[m'.format(idade))
elif idade > 19 and idade <= 25:
    print('O atetla tem \033[33m{}\033[m anos\nE compete na grade \033[30;44mSÊNIOR!!\033[m'.format(idade))
elif idade > 25:
    print('O atetla tem \033[33m{}\033[m anos\nE compete na grade \033[30;44mMASTER!!\033[m'.format(idade))
else:
    print('\033[30;41mNão classificado!!\033[m')