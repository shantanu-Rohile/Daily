def lexicographicallySmallestArray(nums: List[int], limit: int) -> List[int]:
        
        arr = sorted((value, index) for index, value in enumerate(nums))
        groups = []
        group = [arr[0]]

        for i in range(1, len(arr)):
                if arr[i][0] - arr[i-1][0] <= limit:
                        group.append(arr[i])
                else:
                        groups.append(group)
                        group = [arr[i]]

        groups.append(group)

        for group in groups : 
                indices = []
                values = []
                for value , Index in group:
                        indices.append(Index)
                        values.append(value)

                indices.sort()

                for i in range(len(indices)):
                        nums[indices[i]] = values[i]

        
                        

        return nums
        




nums = [1,5,3,9,8]

limit = 2

print(lexicographicallySmallestArray(nums,limit))