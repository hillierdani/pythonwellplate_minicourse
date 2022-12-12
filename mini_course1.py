import pytest

sun: int = 1


@pytest.fixture()
def small():
    limit = 11
    return limit, 'kutyus'


@pytest.fixture()
def large():
    return 101, 'dino'


def test_basics(large):
    print(type(large))
    print(large[1])
    # This is not correct but will not throw an error (only type hint for label, no type check!)
    #
    try:
        # throws exception because mandartory (positional) argument is not specified
        basics(until=large[0])
    except Exception as e1:
        print(e1)
    # second positional argument is actually a named argument, but naming is optional if all previous arguments are set
    results = basics(large[1], large[0])
    try:
        basics(large[1], 'hopsy daisy')
    except Exception as e2:
        # will raise error because we provided a string for until
        print(e2)
    assert results[0] == results[1]


def basics(label: str, until: int, second='hop'):
    """
    Provide squared value of odd numbers.

    Parameters
    ----------
    label
    until: upper limit of range.

    Returns
    -------
    list of ints
    """

    # Produce the square of each odd number between 1 and 1000
    this_is_a_tuple = (1, 1)
    print(second)
    print(type(this_is_a_tuple))
    list1 = (range(1, until))
    print(type(list1))

    list2 = []
    for i in range(len(list1)):
        if i % 2 == 1:
            list2.append(i ** 2)
    print(list2)

    # pythonic way of achieving the same
    list3 = [i ** 2 for i in range(len(list1)) if i % 2 == 1]

    # This will not work: list as key is "unhashable"->dict keys must be hashable-> use tuple (see below)
    # mydict = {'life':'is nice', ['but','or']: ['shit', 'happens']}

    mydict = {'life': 'is nice', ('but', 'or'): ['shit', 'happens']}
    return list2, list3


if __name__ == '__main__':
    basics()
