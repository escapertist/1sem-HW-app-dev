def two_sum(nums: list[int], target: int) -> list[int] | None:
    """Return indices of the two numbers adding up to target (brute force)."""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


if __name__ == "__main__":
    cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
    ]
    for nums, target in cases:
        print(f"nums={nums}, target={target} -> {two_sum(nums, target)}")
