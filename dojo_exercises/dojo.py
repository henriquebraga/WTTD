#coding: utf-8

'''Fizzbuzz dojo'''

from functools import partial

is_multiple_of = lambda base, multiple: multiple % base == 0
is_multiple_of_5 = partial(is_multiple_of, 5) #Cola primeiro parâmetro da função.
is_multiple_of_3 = partial(is_multiple_of, 3) #Cola primeiro parametro da função.

def robot(position):
    say = str(position)
    if is_multiple_of_5(position) and is_multiple_of_3(position):
        say = 'fizzbuzz'
    elif is_multiple_of_3(position):
        say = 'fizz'
    elif is_multiple_of_5(position):
        say = 'buzz'
    return say

'''Happy numbers dojo'''


def happy(number):
    next_ = sum(int(char) ** 2 for char in str(number))
    return number in(1, 7) if number < 10 else happy(next_)


"""
Para definir uma seqüência a partir de um número inteiro o positivo, temos as seguintes regras:
n → n/2 (n é par)
n → 3n + 1 (n é ímpar)
Usando a regra acima e iniciando com o número 13, geramos a seguinte seqüência:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
Podemos ver que esta seqüência (iniciando em 13 e terminando em 1) contém 10 termos. Embora ainda não tenha sido provado (este problema é conhecido como Problema de Collatz), sabemos que com qualquer número que você começar, a seqüência resultante chega no número 1 em algum momento.
Desenvolva um programa que descubra qual o número inicial entre 1 e 1 milhão que produz a maior seqüência.
"""


def next_(n):
    '''Return the next number for the sequence.'''
    return (3 * n + 1) if n % 2 else (n // 2)


def seq(n):
    yield n
    while n > 1:
        n = next_(n)
        yield n


def max_length(start=1, stop=1000001):
    '''Returns the number and length of the longest sequence.'''
    length, number = max((count(seq(n)), n) for n in range(start, stop))
    return number, length


"""
Um homem chamado José é o responsável por ligar e desligar as luzes de um corredor.
Cada lâmpada tem seu próprio interruptor que liga e a desliga. Inicialmente todas as
lâmpadas estão desligadas.

José faz uma coisa peculiar: se existem n lâmpadas no corredor, ele caminha até o fim
do corredor e volta n vezes. Na iésima caminhada, ele aperta apenas os interruptores
aos quais sua posição é divisível por i. Ele não aperta nenhum interruptor na volta à
sua posição inicial, apenas na ida. A iésima caminhada é definida como ir ao fim do
corredor e voltar.

Determine qual é o estado final de cada lâmpada. Está ligada ou desligada?

Exemplo:
Entrada: 3
Saída: [on, off, off]
"""


def light_status(n):
    switches_status = ('off ' * n).split()
    for switch in range(n):
            times_clicked_on_switch = count(num for num in range (1, n + 1) if (switch  + 1) % num == 0)
            if times_clicked_on_switch % 2:
                switches_status[switch] = 'on'
    return switches_status


def count(iterable):
    '''Return how many elements has an iterable.'''
    return sum(1 for _ in iterable)


"""
Jokenpo é uma brincadeira japonesa, onde dois jogadores escolhem um dentre três possíveis itens: Pedra, Papel ou Tesoura.
O objetivo é fazer um juiz de Jokenpo que dada a jogada dos dois jogadores informa o resultado da partida.
As regras são as seguintes:
Pedra empata com Pedra e ganha de Tesoura
Tesoura empata com Tesoura e ganha de Papel
Papel empata com Papel e ganha de Pedra
"""
def jokenpo(player_1, player_2):
    has_player_1_won = lambda game_result: game_result == 2 or game_result == -1
    options = {'rock': 1, 'scissors': 2, 'paper': 3}
    if player_1 not in options or player_2 not in options:
        return 'Sorry, not valid options'
    if player_1 == player_2:
        return 'draw'
    return player_1 if has_player_1_won(options[player_1] - options[player_2]) \
        else player_2


#Tests Happy Numbers dojo
assert all (happy(n) for n in (1, 10, 100, 130, 97))
assert not all(happy(n) for n in(2, 3, 4, 5, 6, 8, 9))

# Tests sequence dojo
assert next_(1) == 4
assert next_(2) == 1
assert next_(13) == 40
assert list(seq(13)) == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
assert count(seq(13)) == 10
assert count(seq(1)) == 1
assert max_length(1, 14) == (9, 20)  # number 9, length 20

#Tests light_status dojo
assert light_status(2) == ['on', 'off']
assert light_status(3) == ['on', 'off', 'off']
assert light_status(4) == ['on', 'off', 'off', 'on']

#Tests for jokenpo dojo

#Tests for invalid options.
assert jokenpo('rack', 'rock') == 'Sorry, not valid options'
assert jokenpo('rock', 'rack') == 'Sorry, not valid options'
assert jokenpo('rock', 'rock') == 'draw'
assert jokenpo('scissors', 'scissors') == 'draw'
assert jokenpo('paper', 'paper') == 'draw'

#Tests when player 1 wins
assert jokenpo('paper', 'rock') == 'paper'
assert jokenpo('scissors', 'paper') == 'scissors'
assert jokenpo('rock', 'scissors') == 'rock'

#Tests when player 2 wins
assert jokenpo('rock', 'paper') == 'paper'
assert jokenpo('paper', 'scissors') == 'scissors'
assert jokenpo('scissors', 'rock') == 'rock'




