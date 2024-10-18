__author__ = "730749520"

from find_max import find_and_remove_max

def run_tests() -> None: # Test 1 return the value
    vals: list[int] = [1,2,3,4,5]
    result: int = find_and_remove_max(vals)
    assert result == 5, f"Expected 5, but got {result}"

    # Edge case
    vals = []
    result= find_and_remove_max(vals)
    assert result == -1, f"Expected -1, but got {result}"

    # When max occurs many times
    vals = [4,4,2,4]
    result= find_and_remove_max(vals)
    assert result == 4, f"Expected 4, but got {result}"
    assert vals == [4,2,4], f"Expected [4,2,4], but got {vals}"

    print("All tests passed!")

if __name__ == "__main__":
    run_tests()


