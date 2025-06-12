# Definition for a pair.
class Pair:
	def __init__(self, key: int, value: str):
		self.key = key
		self.value = value

class Solution:
	def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
		return self.mergeSortHelper(pairs, 0, len(pairs))
	
	def mergeSortHelper(self, pairs: List[Pair], start: int, end: int) -> List[Pair]:
		# if the array only has one element
		if (end - start + 1) <= 1:
			return pairs
		
		middle = (start + end) // 2
		
		# recursively divide till smallest possible subarray
		self.mergeSortHelper(pairs, start, middle)
		self.mergeSortHelper(pairs, middle + 1, end)
		
		# merge the subarrays
		self.mergeArray(pairs, start, middle, end)
		
		return pairs
	
	def mergeArray(self, pairs: List[Pair], start: int, middle: int, end: int) -> None:
		L = pairs[start:middle + 1]
		R = pairs[middle + 1:end + 1]
		
		i = j = 0
		k = start  # start index of k
		
		# merge one by one
		while i < len(L) and j < len(R):
			if L[i].key <= R[j].key:
				pairs[k] = L[i]
				i += 1
			else:
				pairs[k] = R[j]
				j += 1
			
			k += 1
		
		# merge the rest if they exist
		while i < len(L):
			pairs[k] = L[i]
			i, k = i + 1, k + 1
		while j < len(R):
			pairs[k] = R[j]
			j, k = j + 1, k + 1
