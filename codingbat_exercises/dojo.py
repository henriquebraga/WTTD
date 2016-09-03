'''
Escolhendo uma pizza

Contribuição de: Luca Bastos

Você está resolvendo este problema. 
Este problema foi utilizado em 94 Dojo(s).
Em algumas empresas de desenvolvimento de software é comum, quando o prazo de entrega de uma aplicação está próximo, a equipe passar algumas noites trabalhando. E como todo desenvolvedor também precisa se alimentar, eles sempre pedem pizza nessas ocasiões. Só que sempre é uma briga para conseguir escolher os sabores das pizza de sabores que todos gostam.
Um dos membros da equipe, incomodado com as intermináveis discussões sobre o sabor a ser escolhido, resolveu desenvolver um programa para facilitar essa escolha.
Para cada sabor de pizza disponível, cada um deve indicar uma nota para ele (nota 1, se a pessoa detesta o sabor e nota 5 se a pessoa adora o sabor). Depois de processar esses dados, cada pessoa vai saber quais as pessoas que tem o gosto mais parecido que o seu (e que provavelmente irá dividir uma pizza com você).
Por exemplo, para os dados a seguir, o Luca gostaria de saber quem ele deve convidar para dividir uma pizza com ele:
Renato = { Marguerita : 4, Quatro queijos : 5, Escarola : 4, Portuguesa : 5, Frango+Catupiry : 4, Napolitana : 3 }
Marcelo = { Marguerita : 2, Quatro queijos : 2, Escarola : 1, Portuguesa : 3, Frango+Catupiry : 5, Napolitana : 2 }
Lenon = { Marguerita : 4, Quatro queijos : 5, Escarola : 2, Portuguesa : 1, Frango+Catupiry : 1, Napolitana : 3 }
Renata = { Marguerita : 4, Quatro queijos : 5, Escarola : 1, Portuguesa : 1, Frango+Catupiry : 3, Napolitana : 4 }
Washington = { Marguerita : 1, Quatro queijos : 1, Escarola : 2, Portuguesa : 3, Frango+Catupiry : 4, Napolitana : 3 }
Tino = { Marguerita : 1, Quatro queijos : 5, Escarola : 1, Portuguesa : 4, Frango+Catupiry : 3, Napolitana : 2 }
Luca = { Marguerita : 5, Quatro queijos : 4, Escarola : 3, Portuguesa : 4, Frango+Catupiry : 3, Napolitana : 2 }
 '''
def main():
    pizza_options = ('Marguerita', 'Quatro Queijos', 'Escarola', 'Portuguesa', 'Frango+Catupiry', 'Napolitana')
    pizza_rates = tuple(range(1, 6))
    menu()




def menu():
    super_dictionary = {}
    print('Por favor escolha uma opção: ')
    print('1- Cadastrar uma pizza')
    print('2- Informar gostos parecidos e sair')
    read_input = input()
    while read_input == '1':
        name = input('Digite o seu nome'):
        for option in pizza_options:
            key = option
            value = input('Digite sua opção de pizza')
            dictionary_options = sorted(dict(zip('ABCDEF', pizza_options)))
            for pizza_option in dictionary_options:

            sum(1 )    


if __name__ = '__main__':
    main()