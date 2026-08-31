# 2. sum and average

def sum_avg(nums):
    sum = 0
    for i in nums:
        sum += i

    print('Sum  : {} \nAverage : {}'.format(sum,sum/len(nums)))


nums = [7174318734,3123123,3123123,414124124,412414]

sum_avg(nums)