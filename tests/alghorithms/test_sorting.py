import sys
import os

import pytest

from algorithms.sorting import insertion_sort, selection_sort

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


@pytest.mark.parametrize('input_data, expected_output', (
    ([], []),
    ([1], [1]),
    ([9, 7, 6, 5, 3, 2, 1], [1, 2, 3, 5, 6, 7, 9]),
    ([1, 2, 3], [1, 2, 3])
))
def test_insertion_sort(input_data, expected_output):
    """Check if insertion_sort works as expected."""
    assert insertion_sort(input_data) == expected_output


@pytest.mark.parametrize('input_data, expected_output', (
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 5, 7, 6, 9], [9, 7, 6, 5, 3, 2, 1]),
    ([1, 2, 3], [3, 2, 1])
))
def test_insertion_sort_reverse(input_data, expected_output):
    """Check if insertion_sort works as expected."""
    assert insertion_sort(input_data, reverse=True) == expected_output


@pytest.mark.parametrize('input_data, expected_output', (
    ([], []),
    ([1], [1]),
    ([9, 7, 6, 5, 3, 2, 1], [1, 2, 3, 5, 6, 7, 9]),
    ([1, 2, 3], [1, 2, 3])
))
def test_selection_sort(input_data, expected_output):
    """Check if selection_sort works as expected."""
    assert selection_sort(input_data) == expected_output


@pytest.mark.parametrize('input_data, expected_output', (
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 5, 7, 6, 9], [9, 7, 6, 5, 3, 2, 1]),
    ([1, 2, 3], [3, 2, 1])
))
def test_selection_sort_reverse(input_data, expected_output):
    """Check if selection_sort works as expected."""
    assert selection_sort(input_data, reverse=True) == expected_output
