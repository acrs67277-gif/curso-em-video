médida = float(input('Uma distância em metros: '))
cm = médida * 100
mm = médida * 1000
dm = médida * 10
print('A médida entre {}centímetros e {:.0f}milímetros é {:.0f}decímetros. '.format(médida, cm, mm, dm))
km = médida * 1000
hm = médida * 100
dam = médida * 10
print('A médida entre {}quilômetros e {:.0f}hectômetro e {:.0f}decâmetro. '.format(médida, km, hm, dam))

