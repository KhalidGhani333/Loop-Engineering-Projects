from calc import parse_prices, running_total, top_n


def test_parse_prices():
    assert parse_prices("10\n20\n30") == [10.0, 20.0, 30.0]


def test_running_total():
    assert running_total([10, 20, 30]) == [10, 30, 60]


def test_top_n():
    assert top_n([5, 1, 9, 3], 2) == [9, 5]