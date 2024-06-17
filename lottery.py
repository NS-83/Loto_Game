import random


class ComputerPlayer:
    def __init__(self, human, name):
        def sort_card_row_by_tens(card_row):
            """
            Принимает один ряд игровой карты(пять чисел) и сортирует их по десяткам для красивого вывода карты.
            Если в десятке нет чисел, то добавляется пробел
            :param card_row: список из пяти чисел
            :return: Отсортированный по десяткам список из девяти чисел и пробелов
            """

            row_numbers_by_tens = [[] for i in range(0, 9)]
            for number in card_row:
                if number in range(1, 11):
                    row_numbers_by_tens[0].append(number)
                elif number in range(11, 21):
                    row_numbers_by_tens[1].append(number)
                elif number in range(21, 31):
                    row_numbers_by_tens[2].append(number)
                elif number in range(31, 41):
                    row_numbers_by_tens[3].append(number)
                elif number in range(41, 51):
                    row_numbers_by_tens[4].append(number)
                elif number in range(51, 61):
                    row_numbers_by_tens[5].append(number)
                elif number in range(61, 71):
                    row_numbers_by_tens[6].append(number)
                elif number in range(71, 81):
                    row_numbers_by_tens[7].append(number)
                elif number in range(81, 91):
                    row_numbers_by_tens[8].append(number)
            for ten in row_numbers_by_tens:
                sorted(ten)
            card_numbers_sorted_by_tens = []
            for ten in row_numbers_by_tens:
                if ten:
                    card_numbers_sorted_by_tens.extend(ten)
                else:
                    card_numbers_sorted_by_tens.append(' ')
            # В некоторых случаях могут получиться лишние пробелы, убираем их с конца.
            if len(card_numbers_sorted_by_tens) > 9:
                card_numbers_sorted_by_tens.reverse()
                while len(card_numbers_sorted_by_tens) > 9:
                    card_numbers_sorted_by_tens.remove(' ')
                card_numbers_sorted_by_tens.reverse()
            return card_numbers_sorted_by_tens

        player_card_numbers = random.sample(list(range(1, 91)), 15)
        card_first_row = sort_card_row_by_tens(player_card_numbers[:5])
        card_second_row = sort_card_row_by_tens(player_card_numbers[5:10])
        card_third_row = sort_card_row_by_tens(player_card_numbers[10:])
        player_card_numbers.clear()
        player_card_numbers.extend(card_first_row)
        player_card_numbers.extend(card_second_row)
        player_card_numbers.extend(card_third_row)
        self.player_card = player_card_numbers
        self.human = human
        self.name = name
        self.winner = False
        self.loser = False

    def discard_number(self, number):
        if number in self.player_card:
            self.player_card[self.player_card.index(number)] = '-'
        self.winner = self.player_card.count('-') == 15

    def print_card(self):
        def print_card_row(card_row):
            row_string = str(card_row)
            row_string = row_string.replace('[', '')
            row_string = row_string.replace(']', '')
            row_string = row_string.replace(',', '')
            row_string = row_string.replace("'", '')
            print(row_string)

        print('-' * 26)
        print_card_row(self.player_card[:9])
        print_card_row(self.player_card[9:18])
        print_card_row(self.player_card[18:])
        print('-' * 26)


class HumanPlayer(ComputerPlayer):
    def discard_number(self, number, player_choose_discard):
        number_is_in_card = number in self.player_card
        if number_is_in_card:
            self.player_card[self.player_card.index(number)] = '-'
            self.winner = self.player_card.count('-') == 15
        self.loser = number_is_in_card != player_choose_discard


def numbers_input_is_correct(human_players_str, computer_players_str):
    human_players_number = 0
    computer_players_number = 0
    try:
        human_players_number = int(human_players_str)
    except ValueError:
        return False
    try:
        computer_players_number = int(computer_players_str)
    except ValueError:
        return False
    if human_players_number + computer_players_number > 1:
        return human_players_number, computer_players_number
    else:
        return False


if __name__ == '__main__':
    numbers_of_players_input = None
    while not numbers_of_players_input:
        human_players_input = input('Введите количество играющих человек: ')
        computer_players_input = input('Введите количество компьютерных игроков: ')
        numbers_of_players_input = numbers_input_is_correct(human_players_input, computer_players_input)
    number_of_human_players = numbers_of_players_input[0]
    number_of_computer_players = numbers_of_players_input[1]
    players_list = []
    for i in range(number_of_computer_players):
        players_list.append(ComputerPlayer(False, f'Компьютер {i + 1}'))
    for i in range(number_of_human_players):
        player_name = input(f'Введите имя игрока {i + 1}: ')
        players_list.append(HumanPlayer(True, player_name))
    #Для маловероятного случая генерации одинаковых карточек пусть будет список победителей
    winners_list = []
    correct_discard_answers = ['да', 'нет']
    #Победителей может и не быть, если нет компьютерных игроков, а все люди ошиблись
    game_sack = list(range(1, 91))
    while not winners_list and players_list:
        # players_list = list(filter())
        number_from_sack = random.choice(game_sack)
        game_sack.remove(number_from_sack)
        print(f'Выпал номер {number_from_sack}')
        for player in players_list:
            if player.loser:
                continue
            print(player.name)
            player.print_card()
            if player.human:
                answer = None
                while not answer in correct_discard_answers:
                    answer = input('Хотите зачеркнуть номер?(да/нет): ')
                player.discard_number(number_from_sack, answer == 'да')
            else:
                player.discard_number(number_from_sack)
            player.print_card()
            if player.winner:
                winners_list.append(player.name)
        players_list = list(filter(lambda x: not x.loser, players_list))
        if len(players_list) == 1:
            winners_list.append(players_list[0].name)
    if not players_list:
        print('Все игроки ошиблись победителей нет.')
    else:
        print('Победители:')
        for winner in winners_list:
            print(winner)

