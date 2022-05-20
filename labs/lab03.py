sintomas = "Você apresenta pelo menos 4 dos sintomas principais do COVID-19? (Tosse, febre, dor de garganta, congestão nasal, coriza, dor de cabeça, cansaço, dores pelo corpo)"
fezteste = "Você realizou o teste do COVID-19 desde que esses sintomas surgiram?"
contato = "Você entrou em contato recentemente com alguém que foi diagnosticado com o vírus?"
grave = "Você se encontra em estado grave de saúde?"
risco = "Você se enquadra em um grupo de risco? (gestante; portador de doenças crônicas; problemas respiratórios; fumante; pessoa de extremos de idade, seja criança ou idoso)"

distanciamento = "Baseado em suas respostas, a orientação é que você permaneça em distanciamento social"
isolamento = "Baseado em suas respostas, a orientação é que você entre em isolamento"
internado = "Baseado em suas respostas, a orientação é que você vá a um hospital para que possa ser internado"
fazerteste = "Baseado em suas respostas, a orientação é que você vá ao hospital para ser testado para o COVID-19"

file = open("saida.txt", "a")

def faz_pergunta(s):
    print(s, "\n(1) sim\n(2) não", sep = "")
    x = int(input())
    if x != 1 and x != 2:
        print("Opção inválida, recomece a avaliação")
        exit(0)
    return x

x = faz_pergunta(sintomas)
if x == 1:
    print(fezteste, "\n(1) não\n(2) sim, deu positivo\n(3) sim, deu negativo", sep = "")
    x = int(input())
    if x != 1 and x != 2 and x != 3:
        print("Opção inválida, recomece a avaliação")
        exit(0)

    if x == 1:
        print(fazerteste)
    elif x == 2:
        x = faz_pergunta(grave)
        if x == 1:
            print(internado)
        else:
            x = faz_pergunta(risco)
            if x == 1:
                print(internado)
            else:
                print(isolamento)
    elif x == 3:
        print(distanciamento)
else:
    x = faz_pergunta(contato)
    if x == 1:
        print(isolamento)
    else:
        print(distanciamento)