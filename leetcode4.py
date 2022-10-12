def searchRange( nums: list[int], target: int) -> list[int]:
    return [nums.index(target) ,len(nums)-nums[::-1].index(target)-1] if target in nums else [-1, -1]


print(searchRange(nums = [5,7,7,8,8,10], target = 8))











