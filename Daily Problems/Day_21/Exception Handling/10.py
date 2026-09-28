# 10. Handle AttributeError Exception in List Operations

def fun(nums):
    try:
        r = nums.items() 
        print("Length of the list:", r)
    except AttributeError:
        print("Error: The list does not have a 'items' attribute.")

nums = [1, 2, 3]
fun(nums)