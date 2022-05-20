m = float(input())
t = float(input())
n = int(input())

for i in range(n):
    m = m + m * t
    x = float(input())
    while(m + x < 0):
        print("Valor inválido no mês ", i, ". Tente novamente.", sep = "")
        x = float(input())
    m += x

print("O total após ", n, " meses é de R$ ", "{:.2f}".format(m), ".", sep = "")
