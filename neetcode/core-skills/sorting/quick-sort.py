# Definition for a pair.
class Pair:
	def __init__(self, key: int, value: str):
		self.key = key
		self.value = value

class Solution:
	def quickSort(self, pairs: List[Pair]) -> List[Pair]:
		return self.quickSortHelper(pairs, 0, len(pairs) - 1)
	
	def quickSortHelper(self, pairs: List[Pair], start: int, end: int) -> List[Pair]:
		if (end - start + 1) <= 1:
			return pairs
		
		# pick pivot to be the last elements
		pivot = pairs[end]
		left = start
		
		# partition array by placing elements smaller than the pivot on the left side
		for i in range(start, end):
			if pairs[i].key < pivot.key:
				pairs[left], pairs[i] = pairs[i], pairs[left]
				left += 1
		
		# place pivot before the next greater element
		pairs[left], pairs[end] = pivot, pairs[left]
		
		# recursively quick sort the left and right sides
		self.quickSortHelper(pairs, start, left - 1)
		self.quickSortHelper(pairs, left + 1, end)
		
		return pairs
	