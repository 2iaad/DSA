# Data Structures Cheat Sheet

`n` = items, `L` = key length, `S` = total stored characters, `V` = vertices, `E` = edges.
Space means total storage. Times are worst case unless marked **average** or **amortized** (averaged over many operations).

| Data structure | Stored in memory | Why this layout? | Common use | Space | Time complexity |
|---|---|---|---|---|---|
| Array (fixed size) | Consecutive slots | Direct indexing; good cache use | Fixed-size lists, lookup tables | O(n) | Index: O(1); search: O(n); insert/delete with shifting: O(n) |
| Dynamic array | Consecutive slots; larger buffer when full | Fast indexing with room to grow | General lists, resizable buffers | O(n) | Index: O(1); append: O(1) amortized, O(n) worst; search/insert/delete: O(n) |
| Singly linked list | Separate nodes with next pointers | Grow and relink without shifting | Forward traversal, simple chains | O(n) | Access/search: O(n); insert/delete after a known node: O(1) |
| Doubly linked list | Separate nodes with next/previous pointers | Move both ways; remove known nodes easily | LRU caches, navigation history | O(n) | Access/search: O(n); insert beside/delete a known node: O(1) |
| Stack | Dynamic array or linked nodes | Add/remove at one end (LIFO) | Undo, DFS, expression parsing | O(n) | Peek: O(1); push/pop: O(1) with linked nodes, O(1) amortized with dynamic array |
| Queue | Linked nodes with head/tail, or circular buffer | Add at back; remove at front (FIFO) | BFS, task scheduling | O(n) | Front: O(1); enqueue/dequeue: O(1) linked, O(1) amortized with resizable buffer |
| Deque | Doubly linked nodes or circular buffer | Add/remove at either end | Sliding windows, work queues | O(n) | End access: O(1); add/remove at ends: O(1) linked, O(1) amortized with resizable buffer |
| Hash map / hash set | Array of buckets or slots selected by a hash | Jump to likely key location | Key-value lookup, counting, deduplication | O(n) | Search/insert/delete: O(1) average, O(n) worst |
| Balanced BST | Ordered nodes with child pointers; kept balanced | Keep keys sorted and paths short | Ordered maps/sets, range queries | O(n) | Search/insert/delete: O(log n); sorted traversal: O(n) |
| Binary heap | Array representing a complete binary tree | Keep minimum/maximum at root | Priority queues, top-k items | O(n) | Peek: O(1); insert/extract root: O(log n); build: O(n); search: O(n) |
| Trie | Tree of character nodes sharing prefixes | Reuse prefixes; follow keys character by character | Autocomplete, prefix lookup | O(S)* | Search/insert/delete: O(L)*; listing matches adds output cost |
| Graph: adjacency list | Neighbor list for each vertex | Store only existing edges | Sparse networks, BFS/DFS | O(V + E) | List neighbors: O(degree); check edge: O(degree); BFS/DFS: O(V + E) |
| Graph: adjacency matrix | V × V table of edge values | Direct lookup for any vertex pair | Dense graphs, frequent edge checks | O(V²) | Check/add/remove edge: O(1); list neighbors: O(V); BFS/DFS: O(V²) |
| Union-find (DSU) | Parent and rank/size arrays | Group items under shared roots | Connectivity, Kruskal's algorithm | O(n) | Find/union: O(α(n)) amortized with path compression + union by rank/size; nearly constant |

*Trie bounds assume a fixed alphabet and O(1) child lookup. Hash-table bounds assume O(1) hashing and key comparison. An unbalanced BST can take O(n) per operation.*
