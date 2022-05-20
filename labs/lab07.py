class Hero:
	def __init__(self, name, life, damage, block, mana, immediate, passive, activation, insane, star):
		self.name = name
		self.life = life
		self.damage = damage
		self.block = block
		self.mana = mana
		self.immediate = immediate
		self.passive = passive
		self.activation = activation
		self.insane = insane
		self.star = star

def printCard(x):
	if x == 'C':
		print("Cura");
	if x == 'F':
		print("Força");
	if x == 'P':
		print("Proteção");
	if x == 'E':
		print("Éter");
	if x == 'D':
		print("Drenagem");
	if x == 'I':
		print("Insano");
	if x == 'S':
		print("Estrela");

def CardType(x):
	if x == 'C' or x == 'F' or x == 'P' or x == 'E':
		return "IMMEDIATE"
	if x == 'D':
		return "PASSIVE"
	if x == 'I' or x == 'S':
		return "ACTIVATION"

hero = [Hero(name = input(), life = int(input()), damage = int(input()), block = int(input()), mana = int(input()), immediate = ["", "", "", ""], passive = [""], activation = ["", ""], insane = [], star = []), Hero(name = input(), life = int(input()), damage = int(input()), block = int(input()), mana = int(input()), immediate = ["", "", "", ""], passive = [""], activation = ["", ""], insane = [], star = [])]

MAX_LIFE = [hero[0].life, hero[1].life]
MAX_MANA = [hero[0].mana, hero[1].mana]

print("O reino Snowland indicou o herói", hero[0].name)
print("O reino Sunny Kingdom indicou o herói", hero[1].name)

def exec(x):
	x -= 1
	if hero[x].insane != []:
		hero[x].insane[1] -= 1
		if(hero[x].insane[1] == 0):
			hero[x].insane = []
			hero[x].activation[0] = ""

	if hero[x].star != []:
		hero[x].star[1] -= 1
		if(hero[x].star[1] == 0):
			hero[x].star = []
			hero[x].activation[1] = ""

	global MAX_LIFE
	global MAX_MANA
	print("Rodada ", i, ": vez de ", hero[x].name, sep = "")

	card = input().split(" ");
	print(hero[x].name, end = "")
	if card[1] == 'X':
		print(" não encontrou nenhuma carta")
	else:
		print(" encontrou a carta ", end = ""), printCard(card[1])

	if card[1] == 'C':
		if hero[x].mana < int(card[2]):
			print(hero[x].name, "não possui mana suficiente para a mágica")
		else:
			hero[x].mana -= int(card[2])
			hero[x].life += int(card[3])
			hero[x].life = min(MAX_LIFE[x], hero[x].life)
	if card[1] == 'F':
		if hero[x].mana < int(card[2]):
			print(hero[x].name, "não possui mana suficiente para a mágica")
		else:
			hero[x].mana -= int(card[2])
			hero[x].damage += int(card[3])
			hero[x].immediate[1] = 1;
	if card[1] == 'P':
		if hero[x].mana < int(card[2]):
			print(hero[x].name, "não possui mana suficiente para a mágica")
		else:
			hero[x].mana -= int(card[2])
			hero[x].block += int(card[3])
			hero[x].immediate[2] = 1;
	if card[1] == 'E':
		hero[x].mana += int(card[2]);
		hero[x].mana = min(MAX_MANA[x], hero[x].mana)

	if card[1] == 'D':
		if hero[x].passive[0] == "":
			hero[x].passive[0] = int(card[2])
		else:
			print(hero[x].name, " já possui a carta ", sep = '', end = ''), printCard(card[1])

	if card[1] == 'I':
		if hero[x].activation[0] == "":
			hero[x].activation[0] = [int(card[2]), int(card[3]), int(card[4])]
		else:
			print(hero[x].name, " já possui a carta ", sep = '', end = ''), printCard(card[1])
	if card[1] == 'S':
		if hero[x].activation[1] == "":
			hero[x].activation[1] = [int(card[2]), int(card[3])]
		else:
			print(hero[x].name, " já possui a carta ", sep = '', end = ''), printCard(card[1])

	action = input()

	if action == "I":
		if hero[x].insane == [] and hero[x].activation[0] != "" and hero[x].mana >= hero[x].activation[0][0]:
			print(hero[x].name, "ativou a carta Insano")
			hero[x].insane = hero[x].activation[0]
			hero[x].mana -= hero[x].activation[0][0]
		elif hero[x].insane != []:
			print(hero[x].name, "já ativou a carta Insano")
		elif hero[x].activation[0] == "":
			print(hero[x].name, "não possui a carta Insano")
		elif hero[x].mana < hero[x].activation[0][0]:
			print(hero[x].name, "não possui mana suficiente para a mágica")
			

	if action == "S":
		if hero[x].star == [] and hero[x].activation[1] != "" and hero[x].mana >= hero[x].activation[1][0]:
			print(hero[x].name, "ativou a carta Estrela")
			hero[x].star = hero[x].activation[1]
			hero[x].mana -= hero[x].activation[1][0]
		elif hero[x].star != []:
			print(hero[x].name, "já ativou a carta Estrela")
		elif hero[x].activation[1] == "":
			print(hero[x].name, "não possui a carta Estrela")
		elif hero[x].mana < hero[x].activation[1][0]:
			print(hero[x].name, "não possui mana suficiente para a mágica")
			
	
	if action != "A":
		action = input();

	if action == "I":
		if hero[x].insane == [] and hero[x].activation[0] != "" and hero[x].mana >= hero[x].activation[0][0]:
			print(hero[x].name, "ativou a carta Insano")
			hero[x].insane = hero[x].activation[0]
			hero[x].mana -= hero[x].activation[0][0] 
		elif hero[x].insane != []:
			print(hero[x].name, "já ativou a carta Insano")
		elif hero[x].activation[0] == "":
			print(hero[x].name, "não possui a carta Insano")
		elif hero[x].mana < hero[x].activation[0][0]:
			print(hero[x].name, "não possui mana suficiente para a mágica")

	if action == "S":
		if hero[x].star == [] and hero[x].activation[1] != "" and hero[x].mana >= hero[x].activation[1][0]:
			print(hero[x].name, "ativou a carta Estrela")
			hero[x].star = hero[x].activation[1]
			hero[x].mana -= hero[x].activation[1][0]
		elif hero[x].star != []:
			print(hero[x].name, "já ativou a carta Estrela")
		elif hero[x].activation[1] == "":
			print(hero[x].name, "não possui a carta Estrela")
		elif hero[x].mana < hero[x].activation[1][0]:
			print(hero[x].name, "não possui mana suficiente para a mágica")

	if action != "A":
		action = input();

	#ATAQUE
	expected_strength = hero[x].damage

	if hero[x].insane == []:
		print(hero[x].name, "atacou", hero[(x + 1) % 2].name)
	else:
		print(hero[x].name, "deu um ataque insano em", hero[(x + 1) % 2].name)
		expected_strength += hero[x].insane[2];

	if hero[x].passive[0] != "":
		hero[(x + 1) % 2].mana -= hero[x].passive[0]
		hero[(x + 1) % 2].mana = max(hero[(x + 1) % 2].mana, 0)

	if hero[(x + 1) % 2].star != []:
		print(hero[(x + 1) % 2].name, "estava invulnerável")
	else:
		hero[(x + 1) % 2].life -= expected_strength - int((min(hero[(x + 1) % 2].block, 100) * expected_strength) / 100)

i = 1
while hero[0].life > 0 and hero[1].life > 0:
	ok1 = 0
	ok2 = 0
	fodase = input().split(" ")
	if int(fodase[1]) == 1:
		ok1 = 1
		exec(1)
		if hero[1].life > 0:
			fodse = input().split(" ")
			ok2 = 1
			exec(2)
	elif int(fodase[1]) == 2:
		ok2 = 1
		exec(2)
		if hero[0].life > 0:
			fodse = input().split(" ")
			ok1 = 1
			exec(1)
	
		
	if ok1 and ok2:
		print(hero[0].name, " possui ", max(0, hero[0].life), " de vida, ", hero[0].mana, " pontos mágicos, ", hero[0].damage, " de dano e ", min(100, hero[0].block), chr(37)," de bloqueio", sep = '')
		print(hero[1].name, " possui ", max(0, hero[1].life), " de vida, ", hero[1].mana, " pontos mágicos, ", hero[1].damage, " de dano e ", min(100, hero[1].block), chr(37)," de bloqueio", sep = '')

	if hero[1].life <= 0:
		print("O herói", hero[0].name, "do reino Snowland venceu o duelo")
		print(hero[0].name, " possui ", max(0, hero[0].life), " de vida, ", hero[0].mana, " pontos mágicos, ", hero[0].damage, " de dano e ", min(100, hero[0].block), chr(37)," de bloqueio", sep = '')
		print(hero[1].name, " possui ", max(0, hero[1].life), " de vida, ", hero[1].mana, " pontos mágicos, ", hero[1].damage, " de dano e ", min(100, hero[1].block), chr(37)," de bloqueio", sep = '')
	if hero[0].life <= 0:
		print("O herói", hero[1].name, "do reino Sunny Kingdom venceu o duelo")
		print(hero[0].name, " possui ", max(0, hero[0].life), " de vida, ", hero[0].mana, " pontos mágicos, ", hero[0].damage, " de dano e ", min(100, hero[0].block), chr(37)," de bloqueio", sep = '')
		print(hero[1].name, " possui ", max(0, hero[1].life), " de vida, ", hero[1].mana, " pontos mágicos, ", hero[1].damage, " de dano e ", min(100, hero[1].block), chr(37)," de bloqueio", sep = '')

	i += 1