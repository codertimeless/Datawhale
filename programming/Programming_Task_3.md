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

1.3 插入排序

```

```



