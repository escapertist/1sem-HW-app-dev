def two_sum_hashmap(nums: list[int], target: int) -> list[int] | None:
    """Return indices of the two numbers adding up to target (one pass, HashMap)."""
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None


if __name__ == "__main__":
    cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
    ]
    for nums, target in cases:
        print(f"nums={nums}, target={target} -> {two_sum_hashmap(nums, target)}")
