## two heaps
### concept and example
thus far, we have seen how we can solve problems using a single heap. but sometimes the most efficient solution
requires us to use two heaps: both a min and max heap.

let's take a look at a problem that can be solved using the two heaps approach.

finding the median of a continuous stream of numbers is a good example.

    Q: implement a median finder, where new values are inserted into the set, and you have to getMedian from that set.

the naive approach here would be to implement this using a sorted array.
- while we could compute the median in $`O(1)`$ time, insertion would take $`O(n)`$ time as we would need to shift 
elements around to maintain the sorted property.
- using two heaps allows us to still compute the median in $`O(1)`$ time, but now we can also insert elements in
  $`O(log(n))`$ time.

| data structure | insertion   | median |
|----------------|-------------|--------|
| sorted array   | $O(n)$      | $O(1)$ |
| two heaps      | $O(log(n))$ | $O(1)$ |

- #### approach
we will maintain a max-heap and a min-heap.

- in the max-heap, we store the smaller half of values from the stream.
- conversely, in the min-heap, we store the larger half of values from the stream.

to ensure each value goes in the correct heap and both heaps are roughly the same size, we might need to shift some
elements around.

- the max-heap will store the smaller half of the values. thus, the top of the max-heap will be the largest value in the
  smaller half.
- the min-heap will store the larger half of the values. thus, the top of the min-heap will be the smallest value in the
  larger half.

this would mean that the largest value in our max-heap will be smaller than the smallest value in our min-heap. thus,
the median can be calculated by just retrieving the min and the max values from our respective heaps.

if the number of elements in our array is even, both of our heaps will have an equal number of elements. if we have an
odd number of elements, one heap's size will be greater than the other. at any given iteration, the sizes of both heaps
should only differ by at most 1 element.

### examples
- #### odd number of elements
if there are an even number of elements in both the heaps, the median is found by averaging the max from the max-heap 
and the min from the min-heap.

- #### even number of elements
if the number of elements in is odd, the median resides in whichever heap has an extra element.

### implementation
- #### the initial setup
we will start by initializing two heaps in the `Median` class, small and large, denoting our max and min heap, 
respectively.

```python
import heapq as hq

class Median:
  def __init__(self):
    self.small, self.large = [], []
```

- #### insertion
insertion can be performed in $`O(log(n))`$ time into the heap.

    in some languages, max heaps are not supported natively. we can get the behavior of a max heap by using a comparator.
    in Python, we can multiply all of the numbers by -1 to get the desired result.

rather than trying to identify which heap to insert the new element into, we will always insert into the max-heap. it's 
much easier to just rebalance the heaps after the insertion.
- insert the new element into the max-heap.
- if the max from the max-heap is larger than the min-heap, we will shift it to the min-heap.
- if the size of the two heaps differs by more than 1, we will transfer elements between the two heaps to ensure the 
size of the property.

```python
def insert(self, num):
  # push to the max heap and swap with min heap if needed
  hq.heappush(self.small, -1 * num)
  
  if (
    self.small and self.large and
    -self.small[0] > self.large[0]
  ):
    val = -hq.heappop(self.small)
    hq.heappush(self.large, val)

  # handle uneven size
  if len(self.small) > len(self.large) + 1:
    val = -hq.heappop(self.small)
    hq.heappush(self.large, val)
    
  if len(self.large) > len(self.small) + 1:
    val = -hq.heappop(self.large)
    hq.heappush(self.small, val)
```

- #### get median
if the number of elements is odd, and the maxHeap is larger than the minHeap, the median is max in the maxHeap. if the 
minHeap is larger than the maxHeap, the median is the min in minHeap. if the number of elements is even, the median is 
the average of min and max from the respective heaps.

```python
def getMedian(self):
  if len(self.small) > len(self.large):
    return -self.small[0]
  elif len(self.large) > len(self.small):
    return self.large[0]

  # even # of elements, return avg of two middle nums
  return (-self.small[0] + self.large[0]) / 2
```

### time complexities
- insertion: **$O(log(n))$**
- calculate median: **$O(1)$**

### space complexities
- **$O(n)$**, where `n` is the number of elements in the stream.