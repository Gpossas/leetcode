parent = [element for element in range(10)]
rank = [0 for _ in range(len(parent))]

def find(element):
    if parent[element] == element:
        return element
    
    # path compression
    parent[element] = find(parent[element])
    return parent[element]

def find(n):
    p = parent[n]
    while p != parent[p]:
        parent[p] = parent[parent[p]]
        p = parent[p]
    return p

def union(set1, set2):
    smaller = find(set1)
    bigger = find(set2)

    # same set
    if smaller == bigger:
        return
    
    if rank[smaller] > rank[bigger]:
        smaller, bigger = bigger, smaller
    
    parent[smaller] = bigger
    if rank[smaller] == rank[bigger]:
        rank[bigger] += 1

size = [0 for _ in range(len(parent))]

def union(set1, set2):
    smaller = find(set1)
    bigger = find(set2)

    # same set
    if smaller == bigger:
        return
    
    if size[smaller] > size[bigger]:
       smaller, bigger = bigger, smaller
    
    parent[smaller] = bigger
    size[bigger] += size[smaller]