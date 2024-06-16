from lottery import numbers_input_is_correct


def test_numbers_input_is_correct():
    assert numbers_input_is_correct('2', '0')
    assert not numbers_input_is_correct('0', '1')
    assert not numbers_input_is_correct('test', '2')
    assert not numbers_input_is_correct('1.5', '2')
