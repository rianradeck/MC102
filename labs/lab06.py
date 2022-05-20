import math

def Classificacao(x):
	x -= int(math.ceil(x / 3))
	return x

def Prensagem(x):
	if x < 10:
		return 5 * x
	else:
		return 2 * x

def Filtragem(x):
	if x > 45:
		return x - int(math.ceil((9 * x) / 10))
	else:
		return x - int(math.ceil(x / 9))

def Tratamento(x):
	return 2 * x

def PrintWithComma(v):
	print('[', end = '')
	for i in range(len(v)):
		if i == len(v) - 1:
			print(v[i], end = '')
		else:
			print(v[i], end = ', ')
	print(']', end = '')

n = int(input()) #numero de remessas
v = [] #vetor de remessas
p = [0, 0, 0, 0] #vetor de processamento
r = [] #vetor de resultados

for i in range(n):
	v.append(int(input()))
for x in v:
	if x < 2:
		print("É necessário pelo menos dois cajus para produção de cajuína!"), exit(0)

for T in range(n + 5): #Tempo total
	print("T=", T, sep = '', end = ' | ')
	PrintWithComma(v)
	print(" -> ", end = '')
	PrintWithComma(p)
	print(' -> ', end = '')
	PrintWithComma(r)
	print('')

	if p[3] != 0:
		r.append(p[3]) #coloco na resposta o ultimo processamento
	for i in range(3, -1, -1): #vou no vetor de processamento de tras para frente atualizando ele
		if i == 0:
			if T < n :
				p[i] = Classificacao(v[T])
			else:
				p[i] = 0
		if i == 1:
			p[i] = Prensagem(p[i - 1])
		if i == 2:
			p[i] = Filtragem(p[i - 1])
		if i == 3:
			p[i] = Tratamento(p[i - 1])
	if T < n:
		v[T] = 0
