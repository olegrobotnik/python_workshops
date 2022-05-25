# 39.	Создайте программу для игры с конфетами человек против человека.
# Условие задачи:
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте, как наделить бота "интеллектом"

from random import randint
from texttable import Texttable


def intro():
    table = Texttable()
    table.header(["Bachet's game rules"])
    table.add_row([f"We have n = 2021 checkers, and the legal moves are "
                   "\nM = {1, 2, . . . , k = 28} for some 1 ≤ k < 2021."
                   "\nThe winner is the player who takes the last checker."])
    table.set_cols_align(['l'])
    print(table.draw())


def toss_players():
    toss = randint(0, 1)
    players_list = [input("Enter player's 1 name: "), 'Uber bot']
    print(f">>>Your turn, {players_list[toss]}.")
    return players_list, toss


def bachets_game(candies, players_list, toss):
    while candies > 0:
        if players_list[toss] == 'Uber bot':
            candies, toss = uber_bots_turn(candies, players_list, toss)
        else:
            candies, toss = players_turn(candies, players_list, toss)


def players_turn(candies, players_list, toss):
    if candies > 0:
        print(f'>>>Candies on the table: {candies}')
        turn = int(input(f"{players_list[0]}'s turn. Enter the amount of candies from 1 to {max_turn}: "))
        if 1 <= turn <= max_turn and turn <= candies:
            candies -= turn
            if candies == 0:
                print(f'The winner is {players_list[toss]}!')
        else:
            turn = int(input(f">>>Wrong amount!' Enter the amount of candies from 1 to {max_turn}: "))
        toss = not toss
    return candies, toss


def uber_bots_turn(candies, players_list, toss):
    if candies > 0:
        print(f'>>>Candies on the table: {candies}')
        turn = candies % (max_turn + 1)
        if 1 <= turn <= max_turn and turn <= candies:
            if turn == 1:
                print(f">>>Uber bot took {turn} candy.")
            else:
                print(f">>>Uber bot took {turn} candies.")
            candies -= turn
            if candies == 0:
                print(f'The winner is {players_list[toss]}!')
        else:
            turn += 1
            print(f">>>Uber bot took took {turn} candies.")
            candies -= turn
        # else:
        #     print('Wrong amount!')
        #     break
        toss = not toss
    return candies, toss


intro()
players_list, toss = toss_players()
candies = int(input('Enter the amount of candies on the table: '))
max_turn = int(input('Enter the max amount per turn: '))
bachets_game(candies, players_list, toss)
