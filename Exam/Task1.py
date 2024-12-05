
def closest_num_of_zero(nums,n):

    left=0
    right=n-1

    while(left<right):

        if abs(nums[left])<=abs(nums[right]):
            right-=1
        else:
            left+=1
    return abs(nums[left])          

# nums=[-4,-2,1,4,8]
nums=[2,-1,1]

n=len(nums)

print(closest_num_of_zero(nums,n))