# Definition for a pair.
class Pair:
	def __init__(self, key: int, value: str):
		self.key = key
		self.value = value

class Solution:
	def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
		pairStates = []
		
		# start at index 1
		for i in range(len(pairs)):
			j = i - 1  # compare the previous
			
			# while the previous is greater than the next
			while j >= 0 and pairs[j].key > pairs[j + 1].key:
				pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
				j -= 1
			
			# save the clone at the current state
			pairStates.append(pairs[:])
		
		return pairStates
