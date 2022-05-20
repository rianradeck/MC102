# Nesse lab eu irei implementar o merge sort, que eh um algoritmo de ordenacao em tempo O(n * lg n)
# O objetivo eh ordenar cada metade do vetor separadamente e depois jutar elas
# Aprendi esse algoritimo na minha jornada da OBI no ensino medio, ele eh bem util para contar a quantidade de inversoes da ordenacao

INF = 0x3f3f3f3f
NINF = -INF


def ms(v, o):
	if len(v) <= 1:
		return
	# first half, second half
	fh = v[:int(len(v) / 2)]
	sh = v[int(len(v) / 2):len(v)]

	ms(fh, o)
	ms(sh, o)
	fh.append(Pais(chegada = INF, nome = "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ", populacao = NINF, pib = NINF, longevidade = NINF, educacao = NINF, renda = NINF, desigualdade = NINF, idh = NINF))
	sh.append(Pais(chegada = INF, nome = "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ", populacao = NINF, pib = NINF, longevidade = NINF, educacao = NINF, renda = NINF, desigualdade = NINF, idh = NINF))

	p1 = 0
	p2 = 0

	for i in range(len(v)):
		if o == 2:
			if fh[p1].chegada <= sh[p2].chegada:
				v[i] = fh[p1]
				p1 += 1
			else:
				v[i] = sh[p2]
				p2 += 1
		if o == 3:
			if fh[p1].nome <= sh[p2].nome:
				v[i] = fh[p1]
				p1 += 1
			else:
				v[i] = sh[p2]
				p2 += 1
		if o == 4:
			if fh[p1].populacao >= sh[p2].populacao:
				v[i] = fh[p1]
				p1 += 1
			else:
				v[i] = sh[p2]
				p2 += 1
		if o == 5:
			if fh[p1].pib >= sh[p2].pib:
				v[i] = fh[p1]
				p1 += 1
			else:
				v[i] = sh[p2]
				p2 += 1
		if o == 6:
			if fh[p1].idh >= sh[p2].idh:
				v[i] = fh[p1]
				p1 += 1
			else:
				v[i] = sh[p2]
				p2 += 1

class Pais:
	def __init__(self, chegada, nome, populacao, pib, longevidade, educacao, renda, desigualdade, idh):
		self.chegada = chegada
		self.nome = nome
		self.populacao = populacao
		self.pib = pib
		self.longevidade = longevidade
		self.educacao = educacao
		self.renda = renda
		self.desigualdade = desigualdade
		self.idh = idh

	def __str__(self):
		return str(self.nome + " " + str(self.populacao) + " " + str(self.pib) + " " + str(self.idh))

pais = []

t = 0

while(1):
	x = int(input())
	if x not in [1, 2, 3, 4, 5, 6]:
		break
	if x == 1:
		n = int(input())
		for i in range(n):
			linha = input().split(" ")
			pais.append(Pais(chegada = t, nome = linha[0], populacao = int(linha[1]), pib = int(linha[2]), longevidade = int(linha[3]), educacao = int(linha[4]), renda = int(linha[5]), desigualdade = int(linha[6]), idh = int((int(linha[6]) * (int(linha[3]) + int(linha[4]) + int(linha[5]))) / 3)))
			t += 1

			if int(linha[3]) <= 0:
				print("Longevidade fora do intervalo")
				exit(0)
			if int(linha[4]) < 0 or int(linha[4]) > 10:
				print("Educação fora do intervalo")
				exit(0)
			if int(linha[6]) < 0 or int(linha[6]) > 10:
				print("Desigualdade fora do intervalo")
				exit(0)
	if x == 2:
		print("Ordenado por Cadastro")
		ms(pais, 2)
		for x in pais:
			print(x)
	if x == 3:
		print("Ordenado por Nome")
		ms(pais, 3)
		for x in pais:
			print(x)
	if x == 4:
		print("Ordenado por População")
		ms(pais, 4)
		for x in pais:
			print(x)
	if x == 5:
		print("Ordenado por PIB")
		ms(pais, 5)
		for x in pais:
			print(x)
	if x == 6:
		print("Ordenado por IDH")
		ms(pais, 6)
		for x in pais:
			print(x)