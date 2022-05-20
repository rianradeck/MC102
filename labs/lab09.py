#funcao para contar a quantidade de vizinhos em uma posicao de um mapa pupolacional
def count(i, j, grid):
	cnt = 0 # retorno da funcao
	# vetor direcao para olhar os vizinhos
	# -1, 1	    0,1	    1, 1
	# -1, 0	    i,j	    1, 0
	# -1,-1	    0,-1	1, -1
	# dessa forma as posicoes x e x + 1 do vetor vao sempre representar as direcoes
	# exemplo: i + dir[0] = i - 0 e j + dir[1] = j - 1, entao eu estou olhando para o meu vizinho a minha esquerda
	# (mesma linha uma coluna a menos [i, j - 1])
	dir = [0, -1, -1, 0, 1, 1, -1, 1, 0]
	for x in range(len(dir) - 1):
		# [posi, posj] eh a celula de um dos vizinhos de [i, j]
		posi = i + dir[x]
		posj = j + dir[x + 1] 
		if posi < 0 or posi >= n or posj < 0 or posj >= m:
			continue
		if grid[posi][posj] == '+':
			cnt += 1
	return cnt

n = int(input()) # n linhas
m = int(input()) # m colunas
g = int(input()) # geracoes
p = int(input()) # populacao

# crio o mapa populacional que nomeei de grid
grid = []
for i in range(n):
	l = [] # crio uma lista para ser minha linha
	for i in range(m):
		l.append('.') # preencho essa l com M '.'`s
	grid.append(l) # coloco essa linha, entao quando eu olhar grid[0] sera a lista da primeira linha
                   # oq facilitara no acesso de uma celula geral de pos(i, j), pois essa sera grid[i][j]

for i in range(p):
	x = input().split(',')
	grid[int(x[0])][int(x[1])] = '+' # coloco na pos x[0], x[1] uma pessoa

while(g):
	#imprimo o meu mapa populacional para a geracao atual
	for i in range(n):
		for j in range(m):
			print(grid[i][j], end = '')
		print('')
	print('-')

	# crio um novo mapa para ser minha nova populacao, igual a criacao do primeiro mapa
	newgrid = []
	for i in range(n):
		l = [] 
		for i in range(m):
			l.append('.') 
		newgrid.append(l)

	#faco as mudancas da geracao
	for i in range(n):
		for j in range(m):
			neighbourhood = count(i, j, grid)
			
			#se esta em condicao para viver
			if grid[i][j] == '.' and neighbourhood == 3:
				newgrid[i][j] = '+'
			elif grid[i][j] == '+':
				#se esta em condicao para morre
				if neighbourhood < 2 or neighbourhood > 3:
					newgrid[i][j] = '.'
				#senao continua vivo
				else:
					newgrid[i][j] = '+'

	grid = newgrid # atualizo minha variavel grid para meu mapa ser o mapa atualizado da nova geracao
	g -= 1

#imprimo a geracao final
for i in range(n):
		for j in range(m):
			print(grid[i][j], end = '')
		print('')
print("-")