## TASK 4

### 1. HashTable

#### 1.1 为什么要用 **散列表** 这种数据结构呢？

​        在我们进行查找的过程中，很多时候都无法避免要将表中的数据与查找的数据进行比较，看是否是我们需要的值。如果是顺序查找，很显然时间复杂度为 O(n)，而使用其他查找方法如二分查找能够将时间复杂度降至 O(2logn)。

​        在实际的使用中，我们常常会产生这样一种需求：我只关心数据集合中，是否包含这个数据，或者快速获取其相对应的值。如果我们使用上述的方法去处理这个需求，相对来说会比较慢，需要多整个数据集进行多次的比对，遍历。而散列表这种数据结构就很适合处理我们的这一需求，能够将一次查询操作的时间复杂度降为 O(1)，当然这是一种很理想的状态，要求我们的哈希函数足够好，不会产生冲突，但是效率还是要高出很多。

#### 1.2 如何构建哈希表？

​       构造哈希表时，最重要的是哈希函数的设计。

```
数据的哈希地址 = f(关键字的值)
```

​       **数据的哈希地址：**是指在查找表中的存储位置，当我们通过关键字去获取某个表中的值是，实际上是通过哈希地址来访问的，只不过在这中间由程序代替我们，将关键字通过函数转换为哈希地址。

​       **哈希函数：**某种映射关系，即通过该函数，将一个关键字的值（这个值有可能是整数、字符串或者其他信息）通过计算，得到一个哈希地址。

```
example:
张三 13912345678
李四 15823457890
王五 13409872338
赵六 13805834722
```

生活中我们十分常见的电话簿，我们可以自己来考虑一下如何实现，同时要保证高效率，让我们在很快的时间内，找到某个人的电话。如果是使用 Python 来实现的话，就很简单了，我们可以使用Python内置的字典。Python 中字典的底层实现就是散列表，同样的还有集合，但是集合没有关键字索引的功能。

```
>>> name = [("张三", 13912345678), ("李四", 15823457890), ('王五',13409872338), ("赵六",13805834722)]
>>> phone_book = {key:value for key, value in name}
{'张三': 13912345678, '李四': 15823457890, '王五': 13409872338, '赵六': 13805834722}
```

对于像 python 这种高级语言来说，内置的很多数据结构确实能直接帮我们解决很多问题。

那么我们如果使用 C 语言来实现呢，C 语言并没有内置的字典结构，只有我们常用的数组、字符串、整数。这个时候就需要我们自定义哈希函数了。

#### 1.3 如何构造哈希函数？

常用的哈希函数构造方法有 6 种：**直接定址法、数字分析法、平方取中法、折叠法、除留余 数法和随机数法**

​       **直接定址法：**其哈希函数为一次函数

```
H(key) = key 
H(key) = a*key + b
```

​       **数字分析法：**如果关键字有多位字符或者数字组成，就可以考虑抽取其中的 2 位或者多为作为该关键字的哈希地址，在选取关键字的过程中，自然要选取比较多变，不容易重复的。

```
#example:
学号        |  考试成绩
160920143       88
160920144       60
160920145		88
```

如果我们的数据只包含16届的学生，那么我们只需要保留后三位，就能够通过学号查到成绩。

​     **平方取中法：**对关键字做平方操作，取中间得几位作为哈希地址，此方法也是常用的构造哈希函数的方法。

​     **折叠法：**将关键字分割成位数相同的几部分（最后一部分的位数可以不同），然后取这几部分的叠加和（舍去进位）作为哈希地址。此方法适合关键字位数较多的情况。

​      **除留余数法：**若已知整个哈希表的最大长度 m，可以取一个不大于 m 的数记作 p，然后对关键字 key 做取余运算，即 `H(key) = key % p`。

> 在此方法中，对于 p 的取值非常重要，由经验得知 p 可以为不大于 m 的质数或者不包含小于 20 的质因数的合数。

​       **随机数法：**是取关键字的一个随机函数作为它的哈希地址：即 `H(key) = random(key)`，此方法适用于关键字长度不等的情况。

>  注意：这里的随机函数其实是伪随机函数，随机函数是即使每次给定的 key 相同，但是 H（key）都是不同；而伪随机函数正好相反，每个 key 都对应的是固定的 H（key）。

#### 1.4 如何处理冲突？

​        对于哈希表的建立，需要选取合适的哈希函数，但是我们很难去找到一个函数能够完全避免冲突，同时又不会过度的占用时间。我们可以考虑如果设置一个复杂的哈希函数，这样每次在查找时，计算机要经过复杂的运算，那么是划不来的，这样我们的效率就不再接近于 O(1)，是一种得不偿失的方案，只会导致我们的数据结构反而失去了它的特性。

​        通常用的处理冲突的方法有以下几种：

- 开放地址法

​        `H(key) = (H(key) + d) MOD m(其中 m 为哈希表的表长，d 为我们设置的增量)`

​         当我们通过哈希函数得到的哈希地址产生冲突时，通过下面 3 种方法中的一种获取 d 的值，然后继续计算，直到计算出的哈希地址不再冲突为止，这三种获取增量的方式分别为：

​          **1) 线性探测法：**`d = 1, 2, 3...m-1`    方法很简单，既然这个冲突了，那么我们继续往下面找，看看是否还有空的可以存放数据。

​           **2)二次探测法：** `d = 1^2, -1^2, 2^2, -2^2...`   该方法能够有两个方法进行探测，而不是只往后面探测。这样做的好处在于：如果前面有空间，而后面的附近没有空间，使用线性探测效率很低。

​           **3）伪随机数探测法：** d = 伪随机数

- 再哈希法

​       当通过哈希函数求得的哈希地址同其他关键字产生冲突时，使用另一个哈希函数计算，直到冲突不再发生。

- 链地址法

​      将所有产生冲突的关键字所对应的数据全部存储在同一个线性链表中。例如有一组关键字为`{19,14,23,01,68,20,84,27,55,11,10,79}`，其哈希函数为：`H(key)=key MOD 13`，使用链地址法所构建的哈希表所示：

```
0 -> ^
1 -> 01 -> 14 -> 27 -> 79 -> ^
2 -> ^
3 -> 55 -> 68 -> ^
4 -> ^
5 -> ^
6 -> 19 -> 84 -> ^
7 -> 20 -> ^
8 -> ^
9 -> ^
10 -> 10 -> 23-> ^
11 -> 13
12 -> ^
```

- 建立一个公共溢出区

​        建立两张表，一张为基本表，另一张为溢出表。基本表存储没有发生冲突的数据，当关键字由哈希函数生成的哈希地址产生冲突时，就将数据填入溢出表。

#### 1.5 基于链表法解决冲突问题


```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
 
#define N 20      
#define Nhash 7  
#define N_R 200

typedef struct node{
    int key;
    int num;
    struct node * next;
    struct node * pre;
}Node, *Pnode;

typedef struct Hash{
    Pnode link[N]; 
    int num;    
    int len;  
}hash,*Phash;
 
Pnode IniPnode(int key){
    Pnode p=(Pnode)malloc(sizeof(Node));
    p->key=key;
    p->num=1;
    p->next=NULL;
    p->pre=NULL;
}
 
int HashPos(int key){
    return key % Nhash;
}
 
Pnode FindNodePos(Phash h, int key){
    int pos=HashPos(key);
    Pnode link = h->link[pos];
    while(link->next != NULL && link->key != key){
        link=link->next;
    }
    return link;   
}
 
void IniHash(Phash *h, int len){
    int i;
    *h=(Phash)malloc(sizeof(hash));
    for(i=0;i<len;i++){
        (*h)->link[i] = IniPnode(-1);
    }
    (*h)->num =0;  
    (*h)->len=len;
}
 
void Insert(Phash h, int key){
    Pnode p=FindNodePos(h,key);
    if(p->next != NULL) p->num ++;
    else{
        Pnode q =IniPnode(key);
        p->next = q;
        q->pre=p;      
    } 
     ++h->num;
}
 
Pnode Search(Phash h, int key){
    Pnode p=FindNodePos(h,key);
    if(p->next = NULL) return NULL;
    else return p;    
}
 
int Delete(Phash h, int key){
    Pnode p=FindNodePos(h,key);
    p->pre->next=p->next;
    free(p);
} 
 
void PrintLink(Pnode p){
    while(p->next!=NULL){
        printf("[key=%d|num=%d] -> ",p->next->key,p->next->num);
        p=p->next;
    }
    //printf("[key=%d|num=%d]",p->key,p->num);
    printf("\n");
}
 
void PrintHash(Phash h){
    int i;
    printf("哈希表中公有结点%d个\n",h->num);
    for(i=0;i<h->len;i++){
        printf("%d\t",i);
        PrintLink(h->link[i]);
    }
}

void DeleteHash(Phash h){
    int i;
    for(i=0;i<h->num;i++){
        free(h->link[i]);
    }
    free(h); 
}

```

#### 1.6 LRU缓存淘汰算法

```python
from collections import OrderedDict
 
class LRUCache(OrderedDict):
    """
    LRU:Least Recently Used
    
    """

    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = OrderedDict()      # 使用有序字典，否则将随机弹出
     
    def get(self,key):
        if self.cache.has_key(key):
            value = self.cache.pop(key)
            self.cache[key] = value
        else:
            value = None
         
        return value
     
    def set(self,key,value):
        if self.cache.has_key(key):
            value = self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last = False)    # pop出第一个item
                self.cache[key] = value
            else:
                self.cache[key] = value
```

### 2. String

#### 2.1 Tire 树

```python
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for chars in word:
            child = node.data.get(chars)
            if not child :
                node.data[chars] = TrieNode()
            node = node.data[chars]
        node.is_word = True

    def search(self, word):
        node = self.root
        for chars in word:
            node = node.data.get(chars)
            if not node:
                return False
        return node.is_word    # 判断单词是否是完整的存在在trie树中

    def startsWith(self, prefix):
        node = self.root
        for chars in prefix:
            node = node.data.get(chars)
            if not node:
                return False
        return True

    def get_start(self, prefix):
        word_list = []
        if pre_node.is_word:
            word_list.append(pre)
            for x in pre_node.data.keys():
                word_list.extend(get_key(pre + str(x), pre_node.data.get(x)))
       	return word_list
       	
	def get_key(pre, pre_node):
		words = []
        if not self.startsWith(prefix):
            return  words
        if self.search(prefix):
            words.append(prefix)
            return words
        node = self.root
        for chars in prefix:
            node = node.data.get(chars)
        return get_key(prefix, node)
```

