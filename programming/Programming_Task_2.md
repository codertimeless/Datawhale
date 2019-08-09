# TASK 2

## 1. Stack

### 1.1 数组实现顺序栈

```c
#include<stdbool.h>
#define maxsize 10
typedef int datatype;

struct stack
{
    datatype data[maxsize];
    int top;
};
 
typedef struct stack Stack;

void init(Stack *s)
{
    s->top=-1;
}
 
bool Empty(Stack *s)
{
    if(s->top==-1)
    {
        return true;
    }
    else
    {
        return false;
    }
}
 
bool full(Stack *s)
{
    if(s->top==maxsize-1)
    {
        return true;
    }
    else
    {
        return false;
    }
}
 
void Push(Stack *s,datatype element)
{
    if(!full(s))
    {
        s->top++;
        s->data[s->top]=element;
    }
    else
    {
        printf("栈满\n");
    }
}
 
void Pop(Stack *s)
{
    if(!Empty(s))
    {
        s->top--;
    }
    else
    {
        printf("栈空\n");
    }
}
 
datatype Top(Stack *s)
{
    if(!Empty(s))
    {
        return s->data[s->top];
    }
    else
    {
        printf("栈空\n");
    }
}
 
void Destroy(Stack *s)
{
    s->top=-1;
}
```

### 1.2 链表实现链表栈

```c
#include<stdbool.h>
#include<stdlib.h>
typedef int datatype;
 
struct stack
{
    datatype data;
    struct stack *next;
};
 
typedef struct stack Stack;
Stack *s;

void init()
{
    s=NULL;
}
 
bool Empty()
{
    if(s==NULL)
    {
        return true;
    }
    else
    {
        return false;
    }
}

void Push(datatype element)
{
    Stack *p = (Stack *)malloc(sizeof(Stack));
    p->data=element;
    p->next=s;
    s=p;             
}
 

void Pop()
{
    if(!Empty(s))
    {
        s=s->next;
    }
    else
    {
        printf("栈空\n");
    }
}
 
datatype Top()
{
    if(!Empty(s))
    {
        return s->data;
    }
    else
    {
        printf("栈空\n");
    }
}

void Destroy()
{
    free(s);
    s=NULL;
}
```

### 1.3 练习题

#### Valid Parentheses

```
class Solution:
    def isValid(self, s: str) -> bool:
        l = len(s)
        if not l:return True 
        if l == 1:return False
        L = []      
        
        for i in s:
            if i in ("(", "[", "{"):
                L.append(i)
            
            elif i in (")", "]", "}"):
                if L:
                    t = L.pop()
                    
                    if (i == ")" and t == "(") or (i == "]" and t == "[") or (i == "}" and t =="{"):
                        pass
                    else:
                        L.append(t)
                        L.append(i)
                        
                else:
                    L.append(i)
                    
        if L:
            return False
        else:
            return True
```

#### Longest Valid Parentheses

```
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        
        l = len(s)
        dp = [0 for _ in range(l)]
        
        for i in range(1, l):
            if s[i] == "(":
                pass
            
            else:
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                else:
                    if s[i - dp[i-1] - 1] == "(" and i - dp[i - 1] - 1 >= 0:
                        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
        
        
        return max(dp)
        
        
```

#### Evaluate Reverse Polish Notatio

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l = []
        
        for i in tokens:
            if i == "+":
                l.append(int(l.pop(-2)) + int(l.pop()))
            elif i ==  "-":
                l.append(int(l.pop(-2)) - int(l.pop()))
            elif i == "*":
                l.append(int(l.pop(-2)) * int(l.pop()))
            elif i == "/":
                l.append(int(int(l.pop(-2)) / int(l.pop())))
            else:
                l.append(i)

        return l[0]
```



## 2.Queue

### 2.1 数组实现顺序队列

 ```c
//最简单得方式
#include <stdio.h>
int enQueue(int *a,int rear,int data){
    a[rear]=data;
    rear++;
    return rear;
}
void deQueue(int *a,int front,int rear){
    while (front!=rear) {
        printf("出队元素：%d\n",a[front]);
        front++;
    }
}
int main() {
    int a[100];
    int front,rear;
    
    front=rear=0;
    
    rear=enQueue(a, rear, 1);
    rear=enQueue(a, rear, 2);
    rear=enQueue(a, rear, 3);
    rear=enQueue(a, rear, 4);
    
    deQueue(a, front, rear);
    return 0;
}
 ```

### 2.2 链表实现链式队列

```c
#include<stdio.h>
#include<stdlib.h>

typedef struct QNode{
    int data;
    struct QNode * next;
}QNode;

QNode * initQueue(){
    
    QNode * queue=(QNode*)malloc(sizeof(QNode));
    
    queue->next=NULL;
    return queue;
}


QNode* enQueue(QNode * rear,int data){

    QNode * enElem=(QNode*)malloc(sizeof(QNode));
    enElem->data=data;
    enElem->next=NULL;

    rear->next=enElem;

    rear=enElem;
    return rear;
}


void DeQueue(QNode * top,QNode * rear){
    if (top->next==NULL) {
        printf("队列为空");
        return ;
    }
 
    QNode * p=top->next;
    printf("%d",p->data);
    top->next=p->next;
    if (rear==p) {
        rear=top;
    }
    free(p);
}
```

### 2.3 实现一个循环队列

  ```c
#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>

#define true 1
#define false 0
#define BUF_SIZE 8

typedef struct Queue
{
    int * BUF;
    int front;
    int rear;
}QUEUE;

void initQueue(QUEUE *queue_q)
{
    queue_q->BUF = (int *)malloc(sizeof(int)*BUF_SIZE);
    if(queue_q->BUF != NULL)     //队列内存分配成功
    {
        queue_q->front = queue_q->rear = 0; //初始化头尾指针 
    }
   
}

unsigned char isemptyQueue(QUEUE *queue_q)
{
    if(queue_q->front == queue_q->rear)
    {
        return true;
    }
    else
        return false;
}
 
unsigned char is_fullQueue(QUEUE *queue_q)
{
    if((queue_q->rear +1)%BUF_SIZE == queue_q->front)
    {
        return true;
    }else
        return false;
}

 
void In_Queue(QUEUE *queue_q , int value)
{
    if(is_fullQueue(queue_q) != true)        //队列未满
    {
        queue_q->BUF[queue_q->rear] = value;
        queue_q->rear = (queue_q->rear + 1)%BUF_SIZE ;    //尾指针偏移 
    }
}
 
void out_Queue(QUEUE *queue_q , int *value)
{
     if(isemptyQueue(queue_q) != true)        //队列未空
     {
        *value = queue_q->BUF[queue_q->front];
        queue_q->front = (queue_q->front + 1)%BUF_SIZE ;
     }
 }

void bianli_a(QUEUE *queue_q)
{
    if(isemptyQueue(queue_q) != true)
    {
        int ret=queue_q->front;
        while(ret != queue_q->rear)
        { 
            printf("%d  ",queue_q->BUF[ret]);
            ret=(ret+1)%BUF_SIZE;
        }
    }
}

  ```

## 3. Recursive

### 3.1 斐波那契数列求值

```c
def fib(int n)
{
    if(n < 0)
        return 0;
    
    if(n == 0)
        return 0;
    if(n == 1)
    	return 1;
    
    return fib(n-1) + fib(n-2);
}
```

### 3.2 阶乘

```c
def factorial(int n)
{
	if(n < 0)
		return -1;
    if(n == 0)
    	return 1
    
    return factorial(n-1)*factorial(n-2);
}
```

### 3.3 练习题

```c
def climbStairs(int n)
{
    if(n==1)
    	return 1
    if(n==2)
    	return 2
    
    return climbStairs(n-1)+climbStairs(n-2)
   
}
```

