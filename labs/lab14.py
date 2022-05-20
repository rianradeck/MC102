ID = {}
name = {}
action = {}
idcnt = 0
g = []
for i in range(100100):
	g.append([])

n = int(input())
for i in range(n):
	l = input().split(" ")
	# print(l)
	acti = int(l[0])
	nme = l[1];
	friends = l[2:]
	if nme not in ID:
			ID[nme] = idcnt
			name[idcnt] = nme
			idcnt += 1
	for x in friends:
		if x not in ID:
			ID[x] = idcnt
			name[idcnt] = x
			idcnt += 1
	action[ID[nme]] = acti
	for x in friends:
		g[ID[nme]].append(ID[x])

start = 0
for i in range(idcnt):
	if action[i] == 1:
		start = i

fake = [0] * idcnt
def dfs(v):
	fake[v] = 1
	if action[v] != 0:
		for u in g[v]:
			if not fake[u]:
				dfs(u)
dfs(start)

ans = []
for i in range(idcnt):
	if fake[i]:
		ans.append(name[i])
ans.sort()

print("Ordenação por nome");
for x in ans:
	print(x)