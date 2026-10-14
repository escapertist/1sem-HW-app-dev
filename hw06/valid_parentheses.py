def is_valid(s: str) -> bool:
    """Return True if all brackets in s are closed in the correct order (stack)."""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack


if __name__ == "__main__":
    cases = ["()", "()[]{}", "(]"]
    for s in cases:
        print(f'is_valid("{s}") -> {is_valid(s)}')
