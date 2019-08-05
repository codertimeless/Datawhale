

## Task 1: Array and LinkedList

### 1. Basic 

#### 1.1 Array

- 实现一个支持动态扩容的数组，支持增删改操作

```
#通过python实现动态数组

class Arr:
    def __init__(self, capacity=10):
        """
        构造函数
        :param capacity: 数组最大容量，不指定的话默认为10
        """
        self._capacity = capacity
        self._size = 0                                  # 数组有效元素的数目，初始化为0
        self._data = [None] * self._capacity  
 
    def __getitem__(self, item):
        return self._data[item]
 
    def __len__(self):
        return self._size
 
    def getCapacity(self):
        return self._capacity
 
    def isEmpty(self):
        
        return self._size == 0
 
    def add(self, index, elem):
        if index < 0 or index > self._size:     
            raise Exception('Add Filed. Require 0 <= index <= self._size')
        if self._size == self._capacity:        
            self._resize(self._capacity * 2)    
 
        for i in range(self._size - 1, index - 1, -1): 
            self._data[i + 1] = self._data[i]
        self._data[index] = elem        
        self._size += 1                
 
    def get(self, index):
        if index < 0 or index >= self._size:        
            raise Exception('Get failed. Index is illegal.')
        return self._data[index]
 
    def set(self, index, elem):
        if index < 0 or index >= self._size:      
            raise Exception('Sat failed. Index is illegal.')
        self._data[index] = elem
 
    def find(self, elem):
        for i in range(self._size):         # 遍历数组
            if self._data[i] == elem:
                return i                    # 找到就返回索引
        return -1                           
        
    def remove(self, index):
        if index < 0 or index >= self._size:    
            raise Exception('Remove failed.Require 0 <= index < self._size')
        ret = self._data[index]                
        for i in range(index + 1, self._size):  
            self._data[i - 1] = self._data[i]
        self._size -= 1         
        self._data[self._size] = None   
 
        if self._size and self._capacity // self._size == 4:   
            self._resize(self._capacity // 2)
        return ret
```

#### 1.2 LinkedList

- 实现单链表、循环链表、双向链表、支持增删操作

```

class Node:  # create a Node
    def __init__(self, data):
        self.data = data  # given data
        self.next = None  # given next to None


class Linked_List:
    def __init__(self):
        self.Head = None
        
    def insert_tail(self, data):
        if(self.Head is None): 
        	self.insert_head(data)    
        else:
            temp = self.Head
            while(temp.next != None):    
                temp = temp.next
            temp.next = Node(data) 

    def insert_head(self, data):
        newNod = Node(data)    
        if self.Head != None:
            newNod.next = self.Head    
        self.Head = newNod   

    def printList(self):  
        temp = self.Head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def delete_head(self): 
        temp = self.Head
        if self.Head != None:
            self.Head = self.Head.next
            temp.next = None
        return temp
        
    def delete_tail(self):  
        temp = self.Head
        if self.Head != None:
            if(self.Head.next is None):   
                self.Head = None
            else:
                while temp.next.next is not None: 
                    temp = temp.next
                temp.next, tamp = None, temp.next   
        return temp

    def isEmpty(self):
        return self.Head is None  
```

- 实现单链表反转（递归、双指针）

```python
#leetcode ac
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:  return None
        if not head.next:  return head
           
        fast, slow = head, head
        
        while fast and fast.next and fast.next.next:
            fast, slow = fast.next.next, slow.next
            
        right, slow.next =slow.next, None
        left = head
    
        return self.link(self.reverseList(left), self.reverseList(right))
    
    def link(self, left, right):
        r = right
        
        if right == None: return left 
        if left == None:  return right
            
        while r and r.next:
            r = r.next  
            
        r.next = left
        
        return right
```

- 实现求链表的中间结点

```python
#leetcode ac
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        
        while fast and fast.next and fast.next.next:
            fast, slow = fast.next.next, slow.next
        
        return slow if not fast.next else slow.next
```

### 2. Leetcode Exercises

#### Three Sum 

暂时还做出，直接暴力解题会在有很多重复数值时超时。可以使用双指针，将问题简化为：target=-nums[i]-nums[j]，降低时间复杂度；或者使用优先级队列解题，更加简单
#### Majority Element

使用字典...很蠢的方法，但是对于字典的操作不熟悉，所以强行使用字典解题。

```
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        Dict = {}
        
        l = len(nums) // 2
        
        for i in nums:
            if i in Dict:
                Dict[i] += 1
            else:
                Dict[i] = 1
        
        for key,value in Dict.items():
            if value > l:
                return key
```

#### Linked List Cycle I

```
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        
        f, s = head, head
        f = head.next.next
        s = head.next
        
        while f and f.next and f.next.next:
            if f == s:
                return True
            
            else:
              s, f = s.next, f.next.next
        
        return False
```

#### Merge k Sorted Lists

很自然的想到了使用归并，唯一较麻烦的地方在于处理好列表的问题，列表里面嵌套链表。一不小心就容易产生错误的调用。

```
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:return 
        n = len(lists)
        return self.merge(lists, 0, n-1)
    
    def merge(self,lists, left, right):
        if left == right:
            return lists[left]
        
        mid = left + (right - left) // 2
        
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        print(l1,type(l1),'\n',l2,type(l2))
        return self.mergeTwoLists(l1, l2)
    
    def mergeTwoLists(self,l1, l2):
        if not l1:return l2
        if not l2:return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
```

### 3. Summary

（1） 要善于使用双指针，双指针能方便的帮助我们处理很多关于链表的问题，能够更加快速的解决问题；

（2）要善于利用分治法来解决链表合并、排序等问题；

（3）善于利用优先级队列来解决一些有序链表排序的问题，效率高，易于实现；

（4）代码水平仍然存在不足，有时候只求AC，没有去更好的优化和梳理，有待进一步训练。