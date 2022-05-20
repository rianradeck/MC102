clues = {}
country_list = []

def freq(s):
	l = [0] * 26
	for x in s:
		l[ord(x) - ord('a')] += 1
	return l;

s = input()

while(True):
	x = input()
	if x == 'X':
		break;
	ok = 0
	country = ""
	anagram = ""
	l = []
	for u in x:
		if u == ':':
			ok = 1
		if ok == 0:
			country += u;
		if u == ',':
			l.append(anagram)
			anagram = ""
		if ok == 1 and u != ',' and u != ':':
			anagram += u;
	l.append(anagram)
	clues[country] = l
	country_list.append(country)
country_list.append("carmen")
	
print("Iniciando as buscas em", s)

def process(cur_country):
	l = clues[cur_country]
	nxt_country = ""
	cnt = 0
	for i in l:
		cnt += 1
		nxt_country += i

		possible_locations = []
		location = ""
		# print("Estou analisando", cnt, "pistas", nxt_country);
		for j in country_list:
			
			ok = 1;
			cur_freq = freq(j)
			clue_freq = freq(nxt_country)
			for k in range(26):
				if cur_freq[k] < clue_freq[k]:
					ok = 0
			if ok:
				possible_locations.append(j)
				location = j

		# print(possible_locations, location)
		if len(possible_locations) == 1:
			cur_country = location
			break;
		elif cnt == 3:
			# print("CHeguei nas 3 mas a freq n resolveu", nxt_country)
			for x in possible_locations:
				if len(x) == len(nxt_country):
					cur_country = x

	if(cur_country == "carmen"):
		print("Descobri com", cnt, "pistas que Carmen Sandiego está no país");
		return
	print("Descobri com", cnt, "pistas que devo viajar para", cur_country);
	process(cur_country)

process(s)