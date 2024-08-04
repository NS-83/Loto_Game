import pytest

import lottery


@pytest.fixture
def human_game_generator(request):
    new_game = lottery.LotteryGame()
    human_player_card = [x for x in range(1, 16)]
    human_player = lottery.HumanPlayer(True, 'Human', human_player_card)
    new_game.add_player(human_player)
    request.cls.game = new_game


@pytest.mark.usefixtures('human_game_generator')
class TestHumanPlayer:
    def test_str(self):
        name = 'Human'
        card_separator = '--------------------------'
        first_row = '1 2 3 4 5        '
        second_row = '6 7 8 9 10        '
        third_row = '  11 12 13 14 15      '
        computer_player_string = f'{name}\n{card_separator}\n{first_row}\n{second_row}\n{third_row}\n{card_separator}'
        assert str(self.game[0]) == computer_player_string

    def test_right_discard(self):
        self.game[0].discard_number(1, True)
        assert self.game[0]._player_card == ['-', 2, 3, 4, 5, ' ', ' ', ' ', ' ', 6, 7, 8, 9, 10, ' ', ' ', ' ', ' ',
                                             ' ', 11, 12, 13, 14, 15, ' ', ' ', ' ']
        assert not self.game[0].loser
        assert not self.game[0].winner

    def test_discard_wrong_number(self):
        self.game[0].discard_number(16, True)
        assert self.game[0].loser
        assert not self.game[0].winner

    def test_not_discard_right_number(self):
        self.game[0].discard_number(1, False)
        assert self.game[0].loser
        assert not self.game[0].winner

    def test_remove_losers(self):
        self.game[0].discard_number(1, False)
        self.game.remove_losers()
        assert not len(self.game)

    def test_winners_human_wrong_number(self):
        computer_player = lottery.ComputerPlayer(False, 'Computer', [1])
        self.game.add_player(computer_player)
        self.game[0].discard_number(1, False)
        self.game.remove_losers()
        assert self.game.winners() == ['Computer']

    def test_winners_all_numbers_discarded(self):
        computer_player = lottery.ComputerPlayer(False, 'Computer', [x for x in range(2, 17)])
        self.game.add_player(computer_player)
        for i in range(2, 17):
            self.game[1].discard_number(i)
        assert self.game.winners() == ['Computer']

    def test_several_winners(self):
        computer_player = lottery.ComputerPlayer(False, 'Computer', [x for x in range(1, 16)])
        self.game.add_player(computer_player)
        for i in range(1, 16):
            self.game[0].discard_number(i, True)
            self.game[1].discard_number(i)
        assert self.game.winners() == ['Human', 'Computer']
