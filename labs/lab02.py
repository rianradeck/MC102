nome = input()
d = int(input())
v = float(input())

if d > 12:
    m = 1.5
else:
    m = 1.25

if d < 8 or d > 14:
    print("Número de horas diárias não admitido")
else:
    print("O salário do(a) funcionário(a) ", nome, " será de R$", "{:.2f}".format(22 * (8 * v + ((d - 8) * m * v))), " para esse mês", sep = "")
