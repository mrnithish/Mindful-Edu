"""
Given an integer array nums of length n and an integer target,
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 """

def sum3(nums,target):
    subset=[nums[i:j] for i in range(len(nums)) for j in range(i+1,len(nums)+1)]
    r=[]
    for i in subset:
        if len(i)==3:
            r.append(i)
            
    #print(r)
    res=[]
    for j in r:
        if sum(j)>=target:
            res.append(j)
            
    #print(res)
    sums=0

    for i in res:
        sums=sum(i)

    print(sums)

        
            

nums=[-1,2,1,-4]
target=1
sum3(nums,target)

