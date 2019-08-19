## Task 5

### 1. Binary Tree

**树的定义：** 是一种 *一对多* 的数据结构。树(Tree) 是 n（n >= 0）个结点的有限集。n = 0时称为空树。在任意一颗非空树中：

(1) 有且仅有一个特定的称为根（root）的结点；

(2) 当 n = 1时，其余结点可分为 m（m > 0）个互不相交的有限集 T_1, T_2, T_3...T_m，其中每一个集合本身又是一棵树，并且称为根的子树(SubTree)。

**结点分类：** 结点拥有的子树数称为结点的 *度（Degree）*。度为 0 的结点称为 *叶结点（Leaf）*或终端结点；度不为 0 的结点称为非终端结点或分支结点。除根节点之外，分支结点也成为内部结点。树的度是树内各结点中度的最大值。

**树的其他相关概念：**树中结点的最大层次称为树的 *深度（Depth）或高度* ；

如果树中结点的各子树看成从左至右是有序的，则称其为 *有序树*，否则为*无序树* ；

*森林（Forest）*：是 m （m >= 0 颗互不相交的树的集合。

#### 1.1 Binary Search Tree

```python
class TreeNode(object):
    def __init__(self,val):
        self.value = val    #存值
        self.left = None    #存本节点的左子节点
        self.right = None   #存本节点的右子节点
        self.father = None  #存本节点的父节点
        
class BST(object):
    def __init__(self,nodeList):
        self.root = None
        for node in nodeList:
            self.bfs_insert(node)
 
    def bfs_insert(self,node):
        father = None
        cur = self.root
 
        while cur != None:
            if cur.value == node.value:
                return -1
            father = cur
            if node.value < cur.value:
                cur = cur.left
            else:
                cur = cur.right
        node.father = father
        if father == None:
            self.root = node
        elif node.value < father.value:
            father.left = node
        else:
            father.right = node
 
    def bfs(self):
        if self.root == None:
            return None
        retList = []
        q = queue.Queue()
        q.put(self.root)
        while q.empty() is not True:
            node = q.get()
            retList.append(node.value)
            if node.left != None:
                q.put(node.left)
            if node.right != None:
                q.put(node.right)
        return retList
 
    def bfs_search(self,value):
        cur = self.root
        while cur != None:
            if cur.value == value:
                return cur
            elif cur.value < value:
                cur = cur.right
            else:
                cur = cur.left
        return None
 
    def bfs_delete(self,node):
        father = node.father
        if node.left == None:
            if father == None:
                self.root = node.right
                if node.right != None:
                    node.right.father = None
            elif father.left == node:
                father.left = node.right
                if node.right != None:
                    node.right.father = father
            else:
                father.right = node.right
                if node.right != None:
                    node.right.father = father
            return 'delete successfully'
        tmpNode = node.left
        while tmpNode.right != None:
            tmpNode = tmpNode.right
 
        tmpNode.right = node.right
        if node.right != None:
            node.right.father = tmpNode
 
        if father == None:
            self.root = node.left
            node.left.father = None
        elif father.left == node:
            father.left = node.left
            node.left.father = father
        else:
            father.right = node.left
            node.left.father = father
        node = None
        return 'delete successfully'
```

### 2. Heap

```python
class Heap(object):
    def __init__(self,mylist=None):
        self.__size=0
        self.__heaplist=[]
        if type(mylist)==type(self.__heaplist):
            self.__heaplist=mylist
            self.__size = len(mylist)
            self.build_heap()
 
    def is_leaf(self,pos):
        return (pos>=self.__size//2)and(pos<self.__size)
 
    def left_child(self,pos):
        return 2*pos+1
 
    def right_child(self,pos):
        return 2*pos+2
 
    def parent(self,pos):
        return pos//2
 
    def get_size(self):
        return self.__size
 
    def shift_down(self,pos):
        while(not self.is_leaf(pos)):
            min_child=self.left_child(pos)
            rc=self.right_child(pos)
            if (rc<self.__size)and(self.__heaplist[rc]<self.__heaplist[min_child]):
                min_child=rc
            if self.__heaplist[pos]<=self.__heaplist[min_child]:
                return
            self.__heaplist[pos],self.__heaplist[min_child]=self.__heaplist[min_child],self.__heaplist[pos]
            pos=min_child
    
    def push_up(self,pos):
        while (pos !=0) and (self.__heaplist[pos]<self.__heaplist[self.parent(pos)]):
            self.__heaplist[pos],self.__heaplist[self.parent(pos)]=self.__heaplist[self.parent(pos)],self.__heaplist[pos]
            pos=self.parent(pos)
 
    def build_heap(self):
        if self.__size == 0:
            return
        child=self.__size-1
        pnt=self.parent(child)
        for i in range(pnt,-1,-1):
            self.shift_down(i)
 
    def insert(self,data):
        pos=self.__size
        self.__size+=1
        self.__heaplist.append(data)
        self.push_up(pos)
 
    def remove_first(self):
        if self.__size ==0:
            return
        self.__heaplist[self.__size-1],self.__heaplist[0]=self.__heaplist[0],self.__heaplist[self.__size-1]
        self.__size-=1
        if(self.__size !=0):
            self.shift_down(0)
        return self.__heaplist.pop()
 
    def remove_pos(self,pos):
        if self.__size ==0:
            return
        if pos==self.__size-1:
            self.__size-=1
        else:
            self.__heaplist[self.__size - 1], self.__heaplist[pos] = self.__heaplist[pos], self.__heaplist[self.__size - 1]
            self.__size-=1
            self.push_up(pos)
            if self.__size!=0:
                self.shift_down(pos)
        return self.__heaplist.pop()

```

