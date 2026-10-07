# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        res = []
        for i in range(n):
            key = pairs[i]
            j = i - 1

            while j >= 0 and pairs[j].key > key.key:
                pairs[j + 1] = pairs[j]
                j -= 1
            pairs[j + 1] = key
            res.append(pairs[:])
        return res
