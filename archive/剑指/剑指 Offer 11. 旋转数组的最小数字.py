# Solution A:
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        n = len(numbers)
        for i in range(1, n):
            if numbers[i - 1] > numbers[i]:
                return numbers[i]
        return numbers[0]


# Solution B
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        low = 0
        high = len(numbers) - 1
        while low < high:
            mid = (low + high) // 2
            if numbers[mid] < numbers[high]:
                high = mid
            elif numbers[mid] > numbers[high]:
                low = mid + 1
            else:
                high -= 1
        return numbers[low]
