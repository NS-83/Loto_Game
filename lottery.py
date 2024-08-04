import random


class ComputerPlayer:
    def __init__(self, human, name, card_numbers):
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
        card_first_row = sort_card_row_by_tens(card_numbers[:5])
        card_second_row = sort_card_row_by_tens(card_numbers[5:10])
        card_third_row = sort_card_row_by_tens(card_numbers[10:])
        self._player_card = card_first_row + card_second_row + card_third_row
        self._human = human
        self.name = name
        self._winner = False
        self._loser = False

    @property
    def human(self):
        return self._human

    @property
    def loser(self):
        return self._loser

    @property
    def winner(self):
        return self._winner

    def __str__(self):
        def card_row_to_string(card_row):
            row_string = str(card_row)
            row_string = row_string.replace('[', '')
            row_string = row_string.replace(']', '')
            row_string = row_string.replace(',', '')
            row_string = row_string.replace("'", '')
            return row_string
        card_separator = '-' * 26
        first_row = card_row_to_string(self._player_card[:9])
        second_row = card_row_to_string(self._player_card[9:18])
        third_row = card_row_to_string(self._player_card[18:])
        return f'{self.name}\n{card_separator}\n{first_row}\n{second_row}\n{third_row}\n{card_separator}'

    def discard_number(self, number):
        if number in self._player_card:
            self._player_card[self._player_card.index(number)] = '-'
        self._winner = self._player_card.count('-') == 15


class HumanPlayer(ComputerPlayer):
    def discard_number(self, number, player_choose_discard):
        number_is_in_card = number in self._player_card
        if number_is_in_card:
            self._player_card[self._player_card.index(number)] = '-'
            self._winner = self._player_card.count('-') == 15
        self._loser = number_is_in_card != player_choose_discard


class LotteryGame:

    def __init__(self):
        self._players = []

    def add_player(self, player):
        self._players.append(player)

    @staticmethod
    def string_to_int(number_string):
        try:
            return int(number_string)
        except ValueError:
            return 0

    def __len__(self):
        return len(self._players)

    def __str__(self):
        return 'Игроки: '.join(self._players)

    def __getitem__(self, item):
        return self._players[item]

    def winners(self):
        if len(self._players) == 1:
            return [self._players[0].name]
        else:
            winners_filter = filter(lambda x: x.winner, self._players)
            return list(map(lambda x: x.name, winners_filter))

    def remove_losers(self):
        self._players = list(filter(lambda x: not x.loser, self._players))




