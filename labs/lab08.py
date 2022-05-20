class Governo:
	def __init__(self, aprovados = [], recursos = 0, pendentes = []):
		self.aprovados = aprovados
		self.recursos = recursos
		self.pendentes = pendentes

	def Avaliar(self):
		to_remove = []
		for x in self.aprovados:
			x.status = "Pendente"
			self.pendentes.append(x)
		self.aprovados = []
		# print("========= PENDENTES ===========")
		for x in self.pendentes:
			# print(x)
			if x.Apto():
				# print("APROVEI ESSE")
				x.status = "Com auxílio"
				self.aprovados.append(x)
			else:
				# print("NEGUEI ESSE")
				x.negado = 1
				x.status = "Negado"
				to_remove.append(x)
		# print("==============================")
		for x in self.aprovados + to_remove:
			if x in self.pendentes:
				self.pendentes.remove(x)
	def op1(self):
		self.Avaliar()
		print("Beneficiários avaliados\nLista de beneficiários atualizada");

	def AdicionarRecursos(self, x):
		self.recursos += x
	def op2(self, x):
		self.AdicionarRecursos(x)
		print("Recursos adicionados")

	def ImprimeRecursosDisponiveis(self):
		print("Recursos disponíveis: R$", "{:.2f}".format(self.recursos));
	def op3(self):
		self.ImprimeRecursosDisponiveis()

	def ImprimirBeneficiariosAtuais(self):
		print("Beneficiários atuais:")
		for x in self.aprovados:
			print(x.CPF, ": ", x.nome, sep = '')
	def op4(self):
		self.ImprimirBeneficiariosAtuais()

	def EnviarAuxilioMensal(self):
		for x in self.aprovados:
			if self.recursos >= 600:
				x.dinheiro += 600
				x.vezes += 1
				self.recursos -= 600
				if x.vezes >= 3:
					x.status = "Auxílio finalizado"
			else:
				print("Recursos insuficientes")
				return
		print("Auxílio mensal enviado")
	def op5(self):
		self.EnviarAuxilioMensal()

governo = Governo()

def fixedCPF(CPF):
	CPF = list(CPF)
	while(len(CPF) != 14): 
		CPF.append('?')
	for i in range(14):
		if i in [3, 7] and CPF[i] != '.':
			CPF[i + 1:len(CPF)] = CPF[i:len(CPF) - 1]
			CPF[i] = '.'
		if i == 11 and CPF[i] != '-':
			CPF[i + 1:len(CPF)] = CPF[i:len(CPF) - 1]
			CPF[i] = '-'
	CPF = "".join(CPF)
	return CPF

class Beneficiario:
	def __init__(self, nome = " ", CPF = "", status = "", rpc = -1, rtf = -1, idade = 0, emprego = "", vezes = 0, negado = 0, dinheiro = 0):
		self.nome = nome
		self.CPF = CPF
		self.status = status
		self.rpc = rpc
		self.rtf = rtf
		self.idade = idade
		self.emprego = emprego
		self.vezes = vezes
		self.negado = negado
		self.dinheiro = dinheiro

	def __str__(self):
		return "Nome completo: " + self.nome + "\nStatus: " + self.status + "\nCPF: " + self.CPF + "\nRenda per capita: R$ " + str("{:.2f}".format(max(0, self.rpc))) + "\nRenda total: R$ " + str("{:.2f}".format(max(0, self.rtf))) + "\nIdade: " + str(self.idade) + "\nEmprego: " + self.emprego + "\nTempo de recebimento: " + str(self.vezes) + " meses"

	def Apto(self):
		return self.idade >= 18 and self.emprego in ["desempregado", "desempregada", "autonomo", "autonoma", "microempreendedor", "microempreendedora"] and self.vezes < 3 and self.negado == 0 and (self.rpc <= 522.5 or self.rtf <= 3135) and self.status == "Pendente"

	def InserirNome(self, nome):
		self.nome = nome
	def op1(self, nome):
		self.InserirNome(nome)
		print("Nome inserido")

	def InserirCPF(self, CPF):
		CPF = fixedCPF(CPF)
		self.CPF = CPF
	def op2(self, CPF):
		self.InserirCPF(CPF)
		print("CPF inserido")

	def InserirRendaPerCapita(self, rpc):
		self.rpc = rpc
	def op3(self, rpc):
		self.InserirRendaPerCapita(rpc)
		print("Renda per capita inserida")

	def InserirRendaTotalFamiliar(self, rtf):
		self.rtf = rtf
	def op4(self, rtf):
		self.InserirRendaTotalFamiliar(rtf)
		print("Renda total inserida")

	def InserirIdade(self, idade):
		self.idade = idade
	def op5(self, idade):
		self.InserirIdade(idade)
		print("Idade inserida")

	def InserirEmprego(self, emprego):
		self.emprego = emprego
	def op6(self, emprego):
		self.InserirEmprego(emprego)
		print("Emprego inserido")

	def AtualizaStatus(self):
		if self.status in ["", "Perfil incompleto"]:
			if self.nome != " " and self.CPF != "" and self.rpc != -1 and self.rtf != -1 and self.idade != 0 and self.emprego != "":
				self.status = "Perfil completo"
			else:
				self.status = "Perfil incompleto"
	def SolicitarBeneficio(self):
		self.AtualizaStatus()

		if(self.status == "Perfil completo"):
			print("Auxílio solicitado, aguarde avaliação")
			self.status = "Pendente"
			governo.pendentes.append(self)
		if(self.status == "Perfil incompleto"):
			print("Complete seu perfil e tente novamente")
	def op7(self):
		self.SolicitarBeneficio();

	def TransferirBeneficio(self, conta):
		print(("Valor de R$ {:.2f} transferido para a conta corrente {}").format(self.dinheiro, conta))
	def op8(self, conta):
		self.TransferirBeneficio(conta)

	def ImprimeNome(self):
		print("Nome completo:", self.nome)
	def op9(self):
		self.ImprimeNome()

	def ImprimeStatus(self):
		self.AtualizaStatus()
		print("Status:", self.status);
	def op10(self):
		self.ImprimeStatus()

	def ImprimeCPF(self):
		print("CPF:", self.CPF)
	def op11(self):
		self.ImprimeCPF()

	def ImprimirTudo(self):
		self.AtualizaStatus()
		print(self)
	def op12(self):
		self.ImprimirTudo()

beneficiario = []

usuario = [0]
while usuario[0] != 'X':
	usuario = input().split(" ")
	if(usuario[0] == "X"):
		break
	usuario[0] = usuario[0].lower()
	
	if usuario[0] == "governo":
		operacao = [0]
		while operacao[0] != 'F':
			operacao = input().split(" ")
			if operacao[0] == '1':
				governo.op1()
			if operacao[0] == '2':
				governo.op2(float(operacao[1]))
			if operacao[0] == '3':
				governo.op3()
			if operacao[0] == '4':
				governo.op4()
			if operacao[0] == '5':
				governo.op5()
		
	else:
		idx = 0
		if len(usuario) == 1 and idx == 0:
			idx = len(beneficiario)
			beneficiario.append(Beneficiario())
		else:
			for i in range(len(beneficiario)):
				if beneficiario[i].CPF == fixedCPF(usuario[1]):
					idx = i
					break

		operacao = [0]
		while operacao[0] != 'F':
			operacao = input().split(" ")
			if operacao[0] == '1':
				beneficiario[idx].op1((" ".join(operacao[1:])).upper())
			if operacao[0] == '2':
				beneficiario[idx].op2(operacao[1])
			if operacao[0] == '3':
				beneficiario[idx].op3(float(operacao[1]))
			if operacao[0] == '4':
				beneficiario[idx].op4(float(operacao[1]))
			if operacao[0] == '5':
				beneficiario[idx].op5(int(operacao[1]))
			if operacao[0] == '6':
				beneficiario[idx].op6(operacao[1].lower())
			if operacao[0] == '7':
				beneficiario[idx].op7()
			if operacao[0] == '8':
				beneficiario[idx].op8(operacao[1])
			if operacao[0] == '9':
				beneficiario[idx].op9()
			if operacao[0] == '10':
				beneficiario[idx].op10()
			if operacao[0] == '11':
				beneficiario[idx].op11()
			if operacao[0] == '12':
				beneficiario[idx].op12()