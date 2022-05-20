msg = list(input())
p = list(input())

# converto de caracteres na lista para inteiros na lista
def convertstringtoint(s):
	for x in range(len(s)):
		s[x] = int(s[x])

convertstringtoint(msg)
convertstringtoint(p)

# adiciono os 0`s adicionais para a resposta do crc
for i in range(1, len(p)):
	msg.append(0)

# i vai ser o indice que eu estou comecando na minha msg, se ele for diferente de 1 eu continuo,
# senao eu dou xor da msg a partir de i ate i + len(p) - 1, com o p de 0 ate len(p) - 1
i = 0
while i != len(msg) - len(p) + 1:
	if(msg[i] == 1):
		for j in range(i, len(p) + i):
			msg[j] ^= p[j - i]
	i += 1

# excluo os numeros iniciais antes do crc
msg = msg[len(msg) - len(p) + 1:len(msg)]

for x in msg:
	print(x, end = "")
print()