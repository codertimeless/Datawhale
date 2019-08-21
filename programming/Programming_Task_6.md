## TASK６

### 1. The Definition of Graph

​      无论多么复杂的图都是由 **顶点** 和 **边** 构成的。图是由两个集合 *V(vertex)* 和 *E(edge)* 组成，记为       *G = (V, E)* ，其中 V 是顶点的有限集合，记为 *V(G)* ，E是连接 V 中两个不同顶点的边的有限集合，记为  *E(G)* 。

​      在图 G 中，如果表示边的顶点对（或序偶）是有序的，则称 G 为 **有向图(digraph)**。用 <i, j>表示一条从 i 到 j 的有向边，<i, j>, <j, i>是两条不同的边。

​      如果图中的边没有方向，也就是说 <i, j>∈ E(G) 必有 <j, i>∈E(G)，即 E(G) 是对称的，则用 (i, j)表示这两个顶点对，称 G 为无向图。

​       如果图中的每一条边都可以附有一个相对应的数值，这种与边相关的数值称为 **权**。权可以表示从一个顶点到另一个顶点的距离或者花费的代价。边上带有权的图称为 **带权图(weighed graph)**，也称作 **网(net)**。

---

### 2. Storage structure of Graphs

​        图的存储结构除了要存储图中各个顶点本身的信息之外，同时还要存储顶点与顶点之间的所有关系(边的信息)。常用的图的存储结构有 **adjacency matrix(邻接矩阵)** 和 **adjacency list(邻接表)**

#### 2.1  adjacency matrix

图的邻接矩阵是一种采用邻接矩阵数组表示顶点之间相邻关系的存储结构。

```c
typedef struct
{
	int no;                   // 顶点的编号
	InfoType info;			  // 顶点的其他信息
}VertexType;                  // 顶点的类型

typedef struct
{
	int edges[MAXV][MAXV];    // 邻接矩阵数组
	int n, e;                 // 顶点数，边数
	VertexType vexs[MAXV];    // 存放顶点信息
} MatGraph;                   // 完整的图邻接矩阵类型
```

邻接矩阵的特点：

- 图的邻接矩阵是唯一的；
- 邻接矩阵更适合存储边的数目较多的稠密图；
- 无向图的邻接矩阵一定是对称矩阵，为了节省存储空间，可以只保留上三角或下三角部分的元素；
- 对于无向图，邻接矩阵的

#### 2.2  adjacency list

图的邻接表是一种顺序与链式存储相结合的存储方法。

```c
typedef struct ANode
{
	int adjvex;     //该边的邻接点编号
	struct ANode *nextacr;
	int weight; 
}ArcNode;

typedef struct Vnode
{
	InfoType info;
	ArcNode *firstarc;
}VNode;

typedef struct
{
	VNode adjlist[MAXV];
	int n,e;
}AdjGraph;
```

---

### 3. Traversing Graph

#### 3.1 Depth First Search

```python
# Number of Islands 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        
        row = len(grid)
        col = len(grid[0])
        cnt = 0

        def dfs(i, j):
            grid[i][j] = "0" 
            for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == "1":
                    dfs(tmp_i, tmp_j)

        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(i, j)
                    cnt += 1
        
        print(grid)
        return cnt    
```

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print(board)
        columns = [{} for _ in range(9)]
        rows = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                
                if num != ".":
                    num = int(num)
                    box_index = (i//3)*3 + j // 3
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    
                   
                    if rows[i][num] > 1 or columns[j][num] > 1 or 
                    										   boxes[box_index][num] > 1:
                        return False 
        
        return True
```

