from lottery import numbers_input_is_correct, ComputerPlayer, HumanPlayer


def test_numbers_input_is_correct():
    assert numbers_input_is_correct('2', '0')
    assert not numbers_input_is_correct('0', '1')
    assert not numbers_input_is_correct('test', '2')
    assert not numbers_input_is_correct('1.5', '2')


class TestComputerPlayer:

    def test_init(self):
        player = ComputerPlayer(False, 'Test player')
        assert len(player.player_card) == 27
        assert not player.human
        assert not player.loser
        assert not player.winner

    def test_discard_number(self):
        player = ComputerPlayer(False, 'Test player')
        number = None
        player.discard_number(number)
        assert not player.player_card.count('-')
        number_index = None
        for card_number in player.player_card:
            if card_number != ' ':
                number = card_number
                number_index = player.player_card.index(card_number)
                break
        player.discard_number(number)
        assert player.player_card[number_index] == '-'

    def test_winner(self):
        player = ComputerPlayer(False, 'Test player')
        for card_number in player.player_card:
            if card_number != ' ':
                player.discard_number(card_number)
        assert player.winner


class TestHumanPlayer:
    def test_discard_is_right(self):
        player = HumanPlayer(True, 'Test player')
        player.discard_number(91, False)
        assert not player.loser
        number = None
        number_index = None
        for card_number in player.player_card:
            if card_number != ' ':
                number = card_number
                number_index = player.player_card.index(card_number)
                break
        player.discard_number(number, True)
        assert player.player_card[number_index] == '-'
        assert not player.loser

    def test_discard_is_wrong(self):
        player = HumanPlayer(True, 'Test player')
        player.discard_number(91, True)
        assert player.loser
        number = None
        for card_number in player.player_card:
            if card_number != ' ':
                number = card_number
                break
        player.discard_number(number, False)
        assert player.loser
