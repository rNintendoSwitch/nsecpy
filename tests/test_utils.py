from nsecpy import utils


def test_grouper():
    source_data = range(10)

    assert [
        range(0, 5),
        range(5, 10),
    ] == list(utils.grouper(source_data, 5))

    assert [
        range(0, 2),
        range(2, 4),
        range(4, 6),
        range(6, 8),
        range(8, 10),
    ] == list(utils.grouper(source_data, 2))

    assert [
        range(0, 4),
        range(4, 8),
        range(8, 10),
    ] == list(utils.grouper(source_data, 4))
