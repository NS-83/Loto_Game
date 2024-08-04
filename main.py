import random
import sys

from lottery import LotteryGame, ComputerPlayer, HumanPlayer

number_of_computer_players = 0
number_of_human_players = 0
while number_of_human_players + number_of_computer_players < 2:
    computer_players_string = input('Введите количество компьютерных игроков: ')
    number_of_computer_players = LotteryGame.string_to_int(computer_players_string)
    human_players_string = input('Введите количество играющих человек: ')
    number_of_human_players = LotteryGame.string_to_int(human_players_string)
lottery_game = LotteryGame()
for i in range(number_of_computer_players):
    computer_player_name = f'Computer player {i + 1}'
    player_card_numbers = random.sample(list(range(1, 91)), 15)
    new_player = ComputerPlayer(False, computer_player_name, player_card_numbers)
    lottery_game.add_player(new_player)
for i in range(number_of_human_players):
    human_player_name = ''
    while not len(human_player_name):
        human_player_name = input(f'Введите имя игрока {i + 1}: ')
    player_card_numbers = random.sample(list(range(1, 91)), 15)
    new_player = HumanPlayer(True, human_player_name, player_card_numbers)
    lottery_game.add_player(new_player)
game_sack = list(range(1, 91))
while len(game_sack):
    number_from_sack = random.choice(game_sack)
    game_sack.remove(number_from_sack)
    correct_discard_answers = ['да', 'нет']
    print(f'Выпал номер {number_from_sack}')
    for player in lottery_game:
        if player.human:
            print(player)
            answer = None
            while answer not in correct_discard_answers:
                answer = input('Хотите зачеркнуть номер?(да/нет): ')
                player.discard_number(number_from_sack, answer == 'да')
        else:
            player.discard_number(number_from_sack)
            print(player)
    lottery_game.remove_losers()
    if not len(lottery_game):
        print('Все игроки ошиблись победителей нет.')
        sys.exit()
    winners = lottery_game.winners()
    if winners:
        print('Игра окончена. Победители:')
        for winner in winners:
            print(winner)
        sys.exit()


