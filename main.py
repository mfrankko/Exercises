"""
Exercício 15
Nome: Gastos da Viagem
Objetivo: Escrever uma aplicação utilizando funções que calcule os gastos com passagem, hospedagem, aluguel de carro e gastos extras de uma viagem para uma determinada cidade.
Dificuldade: Intermediário
Hospedagem
1 - Crie uma função chamada 'custo_hotel' que receba um parâmetro (argumento) chamado 'noites' e retorne o custo total do hotel, sendo que 1 noite custa R$ 140,00.
Passagem
2 - Crie uma função chamada 'custo_aviao' que receba o nome da cidade e retorne o custo da passagem de avião, sendo que passagem para:
- São Paulo custa R$ 312,00;
- Porto Alegre custa R$ 447,00;
- Recife custa R$ 831,00;
- Manaus custa R$ 986,00.
Aluguel de Carro
3 - Crie uma função chamada 'custo_carro' que receba um parâmetro chamado 'dias'.
- Calcule o custo do aluguel do carro sendo que:
- A cada dia o carro custa R$ 40,00;
- Alugando 7 dias ou +: R$ 50,00 de desconto;
- Alugando 3 dias ou +: R$ 20,00 de desconto;
- Você pode receber apenas um desconto;
- Retorne o custo.
Cálculo Total
4 - Agora com essas três funções criadas, declare uma função que receba a cidade e quantidade de dias e retorne o custo total da viagem.
- Reutilize as funções já criadas.
- Exiba o total da viagem chamando apenas a nova função declarada!
Gastos Extras
5 - Modifique essa nova função criada e adicione um terceiro argumento: 'gastos_extras' e some esse valor ao total da viagem.
Exiba no console o custo total de uma viagem de 12 dias para 'Manaus' gastando R$ 800,00 adicionais.
"""

def custo_hotel(noites):
    return 140 * noites

def custo_aviao(cidade):
    if cidade == 'são paulo':
        return 312
    elif cidade == 'porto alegre':
        return 447
    elif cidade == 'recife':
        return 831
    elif cidade == 'manaus':
        return 986
    else:
        return "Cidade não encontrada"

def custo_carro(dias):
    if dias < 3:
        desconto = 0
    elif dias >= 3 and dias < 7:
        desconto = 20
    elif dias > 6:
        desconto = 50
    custo = (dias * 40) - desconto
    return custo

def viagem(noites, cidade, dias, gastos_extra):
    return custo_carro(dias) + custo_aviao(cidade) + custo_hotel(noites) + gastos_extra

cidade = input('Coloque a cidade para qual você vai viajar ').lower()
dias = int(input('Coloque quantos dias você usará o carro '))
noites = int(input('Coloque quantas noites você passará na cidade '))
gastos_extras = float(input('Coloque o valor dos gastos extras '))

custo = viagem(noites, cidade, dias, gastos_extras)

print("O custo total para ir para {}, ficar {} noites, usar o carro por {} dias e gastar R$ {:.2f} a mais é de R$ {:.2f}".format(cidade, noites, dias, gastos_extras, custo))