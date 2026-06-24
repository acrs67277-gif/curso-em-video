nome = str(input('Qual é seu nome? ')).split()
print('Seu nome tem Silva? {} '.format('SILVA' in nome.upper()))
print('Seu nome tem Silva? {} '.format('silva' in nome.lower()))
print('Seu nome tem Silva? {} '.format('Silva' in nome.capitalize()))

