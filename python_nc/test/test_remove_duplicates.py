import pytest
from ..remove_duplicates import Solution

@pytest.fixture
def solution():
    return Solution()

def test_remove_duplicates_case1(solution):
    nums = [1, 1, 2]
    expected_length = 2
    assert solution.removeDuplicates(nums) == expected_length
    assert nums[:expected_length] == [1, 2]

def test_remove_duplicates_case2(solution):
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected_length = 5
    assert solution.removeDuplicates(nums) == expected_length
    assert nums[:expected_length] == [0, 1, 2, 3, 4]

def test_remove_duplicates_case3(solution):
    nums = [1, 1, 1, 1, 1]
    expected_length = 1
    assert solution.removeDuplicates(nums) == expected_length
    assert nums[:expected_length] == [1]

def test_remove_duplicates_case4(solution):
    nums = []
    expected_length = 0
    assert solution.removeDuplicates(nums) == expected_length
    assert nums[:expected_length] == []

def test_remove_duplicates_case5(solution):
    nums = [1, 2, 3, 4, 5]
    expected_length = 5
    assert solution.removeDuplicates(nums) == expected_length
    assert nums[:expected_length] == [1, 2, 3, 4, 5]
