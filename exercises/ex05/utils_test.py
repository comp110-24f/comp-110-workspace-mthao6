__author__ = "730749520"

import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index

def test_only_even_no_evens():
    """Test when there are no even nums"""
    assert only_evens([1,3,5]) == []

def test_only_evens_some_evens():
    """Test when there are some even nums"""
    assert only_evens([1,2,3,4]) == [2,4]

def test_only_evens_empty():
    """Test when input list is empty"""
    assert only_evens([]) == []

# Test for sub

def test_sub_normal():
    """Test w normal start and end range"""
    assert sub ([10,20,30,40], 1,3) == [20,30]

def test_sub_negative_start():
    """When start is negative"""
    assert sub([10,20,30,40], -1,2) == [10,20]

def test_sub_empty_input():
    """When input list is empty"""
    assert sub([], 0, 2) == []

# Test for add_at_index

def test_add_at_index_middle():
    vals = [10,20,30]
    add_at_index(vals, 25, 2)
    assert vals == [10,20,25,30]

def test_add_at_index_end():
    vals = [10,20]
    add_at_index(vals, 30, 2)
    assert vals == [10, 20, 30]

def test_add_at_index_raises_indexerror():
    vals = [10,20,30]

    with pytest.raises(IndexError):
        add_at_index(vals, 40, 5) # Idx 5 is out of bounds for a list w 3 elems