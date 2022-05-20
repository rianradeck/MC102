# Vamos criar a funcao de binary insertion sort
# Aprendi lendo esse artigo: https://www.geeksforgeeks.org/binary-insertion-sort/
def ordenar(v):
	for i in range(1, len(v)):
		bg = 0
		nd = i
		while bg < nd:
			mid = (bg + nd) >> 1
			if v[mid] < v[i]:
				bg = mid + 1
			else:
				nd = mid
		aux = v[i]
		v[nd + 1:i + 1] = v[nd:i]
		v[nd] = aux

#retorna o vetor de cartas em fomato de par de inteiros
#utilizei isso para evitar criar uma classe Carta com a funcao __lt__ para a funcao de ordenacao funcionar
def fix(v):
	if len(v) == 0:
		return []
	for i in range(len(v)):
		if v[i][0] == '1' and v[i][1] == '0':
			v[i] = (10, 0 if v[i][2] == 'C' else 1 if v[i][2] == 'E' else 2 if v[i][2] == 'O' else 3 if v[i][2] == "P" else int(v[i][2]))
		else:
			v[i] = (1 if v[i][0] == 'A' else 11 if v[i][0] == 'J' else 12 if v[i][0] == 'Q' else 13 if v[i][0] == 'K' else int(v[i][0]), 0 if v[i][1] == 'C' else 1 if v[i][1] == 'E' else 2 if v[i][1] == 'O' else 3 if v[i][1] == "P" else int(v[i][1]))
	return v

#funcao para printar de pares para o modo original de numeros e letras
def printa(v):
	for a, b in v:
		print(' ', 'J' if a == 11 else 'Q' if a == 12 else 'K' if a == 13 else 'A' if a == 1 else a, 'C' if b == 0 else 'E' if b == 1 else 'O' if b == 2 else 'P', sep = '', end = '')

bot = input()
if bot != "":
	bot = fix(bot.split(" "))
else:
	bot = []

pilha = input()
if pilha != "":
	pilha = fix(pilha.split(" "))
else:
	pilha = []
alvo = input()
jogada = []
alvo = 1 if alvo == 'A' else 11 if alvo == 'J' else 12 if alvo == 'Q' else 13 if alvo == 'K' else int(alvo)
challenge = input()

ok = 0
for a, b in bot:
	if a == alvo:
		pilha.append((a, b))
		jogada.append((a, b))
		ok = 1
k = 0
if not ok:
	while k < len(bot) and bot[k][0] == bot[0][0]:
		jogada.append(bot[k])
		pilha.append(bot[k])
		k += 1
for x in pilha:
	try:
		bot.remove(x)
	except ValueError:
		continue

if challenge == 'S':
	if not ok:
		bot = bot + pilha
	pilha = []

bot = fix(bot)
pilha = fix(pilha)

ordenar(bot)
print("Jogada:", end = ' ' if len(jogada) == 0 else '')
printa(jogada)
print("\nUm bot adversário duvidou" if challenge == 'S' else "\nNenhum bot duvidou")
if challenge == 'S':
	print("O bot estava blefando" if ok == 0 else "O bot não estava blefando")
print("Mão:", end = ' ' if len(bot) == 0 else '')
printa(bot)
print("\nPilha:", end = ' ' if len(pilha) == 0 else '')
printa(pilha)
if len(bot) == 0:
	print("\nO bot venceu o jogo")
else: 
	print("")