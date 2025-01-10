def rotate(nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        part_1 = nums[-k:]
        part_2 = nums[0:len(nums)-k]
        result = part_1 + part_2
        return result


list1 = [1,2,3,4,5,6,7]
k1 = 3

print(rotate(list1, k1))