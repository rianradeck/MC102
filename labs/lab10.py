from PontStop import *

def fix_list(lista):
	lista = lista.lower().split(" ")
	lista = sorted(lista)
	lista = lista[::-1]
	while lista[len(lista) - 1] == '':
		lista = lista[:-1]
	for i in range(len(lista)):
		temp = ""
		for j in range(len(lista[i])):
			if lista[i][j] not in pontuacoes:
				temp += lista[i][j]
		lista[i] = temp

	temp = []
	for x in lista:
		if x not in stop_words:
			temp.append(x)
	lista = temp
	temp = []

	for x in lista:
		temp.append(sinonimos.get(x, x))
	lista = temp

	lista = list(set(lista))
	lista = sorted(lista)
	return lista

linha = input()
sinonimos = {}

while(linha != '}'):
	f1 = 0
	sinonimo = ""
	representante = ""
	linha = input()
	if linha == '}':
		break
	for i in range(len(linha)):
		if linha[i] == ':':
			f1 = 1
			continue
		if f1 == 0:
			representante += linha[i]
		elif linha[i] != ',':
			sinonimo += linha[i]
		if linha[i] == ',' or i == len(linha) - 1:
			sinonimos[sinonimo] = representante
			sinonimo = ""

pergunta_original = input()
pergunta = fix_list(pergunta_original)
print("Descritor pergunta:", ','.join(pergunta))

ans = 0
max_intersection = 0
n = int(input())
resposta_original = [None] * (n + 1)
resposta_original[0] = 42
resposta = [None] * (n + 1)
for i in range(1, n + 1):
	resposta_original[i] = input()
	resposta[i] = fix_list(resposta_original[i])
	if len(list(set(pergunta).intersection(resposta[i]))) == len(pergunta):
		ans = i
	print("Descritor resposta " , i, ": ", ','.join(resposta[i]), sep = '')

print("\nA resposta para a pergunta ", "\"", pergunta_original, "\"", " é ", "\"", resposta_original[ans], "\"", sep = '')