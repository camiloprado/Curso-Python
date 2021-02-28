print('{:=^40}'.format('PAGAMENTO'))
total = float(input('Informe o total a ser pago: R$'))
print('Qual será a forma de pagamento?\n'
      '[ 1 ] à Vista (DINHEIRO/CHEQUE)\n'
      '[ 2 ] à Vista no CARTÃO\n'
      '[ 3 ] 2x no CARTÃO\n'
      '[ 4 ] 3x ou mais no CARTÃO')
escolha = int(input('Opção: '))
if escolha == 1:
    desconto = total * 0.1
    pagar = total - desconto
    print('Terá desconto de 10%\n'
          'Logo pagará: R${:.2f}'.format(pagar))
elif escolha == 2:
    desconto = total * 0.05
    pagar = total - desconto
    print('Terá desconto de 5%\n'
          'Logo pagará: R${:.2f}'.format(pagar))
elif escolha == 3:
    print('O valor será pago em 2x de R${:.2f}'.format(total/2))
    print('Logo pagará: R${:.2f}'.format(total))
elif escolha == 4:
    juros = total * 0.2
    pagar = total + juros
    print('Terá juros de 20%\n'
          'Logo pagará: R${:.2f}'.format(pagar))
else:
    print('\033[0;30;41mEscolha não encontrada!!\033[m')