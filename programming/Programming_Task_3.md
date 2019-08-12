# TASK 3

## 1. SORTING

### 1.1 Merge Sort

```python
def mergesort(nums):
    l = len(nums)
    if l == 1:
        return nums
    
    mid = l // 2
    left, right = nums[:mid], nums[mid:]
    return merge(mergesort(left), mergesort(right))

def merge(left, right):
    res = []

    while left and right:
        l, r = left[0], right[0]
        if l > r:
            res.append(right.pop(0))
        else:
            res.append(left.pop(0))

    res += left if left else right
    return res
```

### 1.2 Quick Sort

```python
def quick_sort(nums, left, right):
    if left >= right:
        return 
    head = left
    rear = right
    temp = nums[left]
    
    while left < right:
        while left < right and nums[right] > temp:
            right -= 1
        nums[left] = nums[right]  
        while left < right and nums[left] <= temp:
            left += 1
        nums[right] = nums[left]
        nums[left] = temp
    quick_sort(nums, head, left - 1)
    quick_sort(nums, left + 1, rear)
```

### 1.3 Insect Sort

```python
def insectsort(array):
    l = len(array)
    print(l)
    
    if l == 0 or l == 1:
        return 
    
    for i in range(1,l):
        key = array[i]
        j = i - 1
        
        while (array[j] > key) and (j >= 0):
            array[j+1] = array[j]
            print("arrray[%s] -> array[%s]" %(j,j+1))
            j -= 1
        
        array[j+1] = key
    
```

### 1.4 Select Sort

```python
def selectsort(array):
    l = len(array)
    if l == 0 or l == 1:
        return 
    
    for i in range(0,l-1):
        min = i
        for j in range(i+1,l):
            if array[j] < array[min]:
                min = j
        
        array[i], array[min] = array[min], array[i]
        
        
```

### 1.5 Bubble Sort

```
def bubblesort(array):
    l = len(array)
    if l == 0 or  l == 1:
        return 
    
    for i in range(l-1):
        for j in range(l-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    
    
```

### 1.6 Heap Sort

```python
def buildMaxHeap(array):
    for i in range(len(array)//2, -1, -1):
        heapify(array, i)

def heapify(array, i):
    left = 2*i + 1
    right = 2*i + 2
    largest = i
    if left < arrlen and array[left] > array[largest]:
        largest = left
    if right < arrlen and array[right] > array[largest]:
        largest = right
    
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, largest)

def Heapsort(array):
    global arrlen
    arrlen = len(array)
    
    buildMaxHeap(array)
    for i in range(len(array)-1,0,-1):
        array[0], array[i] = array[i], array[0]
        arrlen -= 1
        heapify(array, 0)
    return array

```

## 2. BINARY SEARCH

### 2.1 Implementing Binary Search of an Ordered Array

```python
def binarySearch(nums, key):
	l = len(nums)
	i, j = 0, l - 1
	
	while(i <= j):
		mid = (i + j) // 2
		if key > nums[mid]:
			i = mid + 1
		elif key < nums[mid]:
			j = mid - 1
		else:
			return mid
	
	return None
	
```

```python
def fuzzyBinarysearch(nums,key):
	if not nums:
		return
	if key > nums[-1]:
        return
    if num <= nums[0]:
        return 0
    elif num == nums[-1]:
        return len(nums) - 1
    
    low = 0
    high = len(nums) - 2
    while low <= high:
        mid = (high + low) // 2
        if key > nums[mid] and key <= nums[mid + 1]:
            return mid + 1
        elif key > nums[mid + 1]:
            low = mid + 1
        elif key <= nums[mid]:
            high = mid
     return 


```

### 2.2 Sliding Window Maximum

```python
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if not nums:
            return []
        if k == 1:
            return nums
        
        def clean_deque(i):
            if deq and deq[0] == i - k:
                deq.popleft()
            
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
       
        deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]
        
        for i in range(k, n):
            clean_deque(i)          
            deq.append(i)
            output.append(nums[deq[0]])
        return output
```

### 2.3 Sqrt(x)

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if not x: return 0
        if x < 3: return 1
        
        low = 0
        high = x 
        mid = high // 2
        
        while high - low > 1:
            tem = mid**2
         
            if tem == x:
                return mid    
            if tem > x:
                high = mid
                mid = (low + high) // 2
            if tem < x:
                low = mid
                mid = (high + low) // 2
    
        return mid
```

