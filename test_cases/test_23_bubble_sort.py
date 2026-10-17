
from importlib import import_module

module = import_module("23_bubble_sort")
bubble_sort = module.bubble_sort


def test_unsorted_list():
    assert bubble_sort([5, 2, 8, 1, 3]) == [1, 2, 3, 5, 8]


def test_sorted_list():
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]


def test_reverse_list():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]


def test_duplicates():
    assert bubble_sort([3, 1, 3]) == [1, 3, 3]


def test_empty_list():
    assert bubble_sort([]) == []


def test_single_element():
    assert bubble_sort([7]) == [7]


def test_original_list_unchanged():
    numbers = [3, 1, 2]
    bubble_sort(numbers)
    assert numbers == [3, 1, 2]

