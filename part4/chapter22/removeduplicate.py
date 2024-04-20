def removeDuplicate(nums: list[int]) -> int:
    nums[:] = sorted(set(nums))
    return len(nums)
