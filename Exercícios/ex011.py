largura = float(input('Qual largura da parede? '))
altura = float(input('Qual altura da parede? '))
area = largura * altura
print('Sua parede tem a dimensão de {} x {} área {}m²'.format(largura, altura, area))
tinta = area /2
print('Para pintar essa parede, você precisará de {}l de tinta. '.format(tinta))
