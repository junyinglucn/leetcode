class Solution:
    def minArray(self, numbers: List[int]) -> int:
        n = len(numbers)
        for i in range(1, n):
            if numbers[i - 1] > numbers[i]:
                return numbers[i]
        return numbers[0]
