def find_duplicate(nums):
    seen = set()
    for num in nums:
        if isinstance(num, str):
            return False
        elif num < 0:
            return False
        elif num in seen:
            return num
        seen.add(num)
    return False
    raise NotImplementedError
