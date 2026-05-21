real = float(input('Quantos reais você na carteira? R$ '))
dolar = real / 5.43
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
