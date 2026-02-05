def fourSum(nums: list[int], target: int) -> list[list[int]]:
    new_nums = sorted(nums)
    triplet_arr = []
    i = 0
    n_len = len(nums)
    while i < n_len - 4:
        j = 1
        while j < n_len - 3:
            left = i + 2
            right = n_len - 1
            if left!=right:
                if ((new_nums[i]+new_nums[j]+new_nums[left]+new_nums[right]) == target) and ([new_nums[i], new_nums[j], new_nums[left], new_nums[right]] not in triplet_arr):
                    triplet_arr.append([new_nums[i], new_nums[j], new_nums[left], new_nums[right]])
                elif (new_nums[i]+new_nums[j]+new_nums[left]+new_nums[right]) < target:
                    left += 1
                elif (new_nums[i]+new_nums[j]+new_nums[left]+new_nums[right]) > target:
                    right -= 1
            j += 1
        i += 1
    return triplet_arr
            
example_arr = [1, 0, -1, 0, -2, 2]
tar = 0
ans = fourSum(example_arr, tar)
print(ans)