def sum2(nums):
    if len(nums) <= 2:
        tot = nums[0] + nums[1]
        print(tot)
    tot = 0
    for i in nums:
        tot = i + tot
    print(tot)
sum2([1])
sum2([1,2,4,5])
