from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_get_negative():
    assert arrs.get([1, 2, 3], -1, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]


def test_slice_empty():
    assert arrs.my_slice([], 1, 3) == []


def test_slice_negative_start():
    assert arrs.my_slice([1, 2, 3, 4], -1) == [4]

