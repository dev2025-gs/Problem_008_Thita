def fourSum(nums: list[int], target: int) -> list[list[int]]:
    new_nums = sorted(nums)
    triplet_arr = []
    i = 0
    n_len = len(nums)
    if n_len == 4:
        if (new_nums[0]+new_nums[1]+new_nums[2]+new_nums[3]) == target:
            triplet_arr.append([new_nums[0], new_nums[1], new_nums[2], new_nums[3]])
    else:
        while i < n_len - 4:
            j = i + 1
            while j < n_len - 3:
                left = j + 1
                right = n_len - 1
                while left!=right:
                    if ((new_nums[i]+new_nums[j]+new_nums[left]+new_nums[right]) == target) and ([new_nums[i], new_nums[j], new_nums[left], new_nums[right]] not in triplet_arr):
                        triplet_arr.append([new_nums[i], new_nums[j], new_nums[left], new_nums[right]])
                        left += 1
                    elif (new_nums[i]+new_nums[j]+new_nums[left]+new_nums[right]) < target:
                        left += 1
                    elif (new_nums[i]+new_nums[j]+new_nums[left]+new_nums[right]) > target:
                        right -= 1
                    else:
                        left += 1
                j += 1
            i += 1
    return triplet_arr
            
example_arr = [1, 0, -1, 0, -2, 2]
tar = 0
ans = fourSum(example_arr, tar)
print(ans)

example_arr_2 = [0, 0, 0, 0]
tar_1 = 0
ans_2 = fourSum(example_arr_2, tar_1)
print(ans_2)
