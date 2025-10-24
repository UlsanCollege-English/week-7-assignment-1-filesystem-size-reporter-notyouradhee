from collections import deque

class Node:
    def __init__(self, name, size=0, children=None):
        self.name = name
        self.size = size
        self.children = children or []

def total_size(node):
    # TODO: postorder sum
    if not node:
        return 0
    
    size = node.size
    
    for child in node.children:
        size += total_size(child)
        
    return size

def folder_sizes(root):
    # TODO: return dict {folder_name: total_bytes}
    if not root:
        return {}

    sizes_map = {}

    def dfs_helper(node):
        current_size = node.size
        is_directory = bool(node.children)
        
        for child in node.children:
            current_size += dfs_helper(child)
        
        if is_directory:
            sizes_map[node.name] = current_size
            
        return current_size

    dfs_helper(root)
    
    if root.name in sizes_map:
        del sizes_map[root.name]
        
    return sizes_map

def level_order(root):
    # TODO: BFS levels, return list of lists of names
    if not root:
        return []
    
    results = []
    queue = deque([root]) 
    
    while queue:
        level_size = len(queue)
        current_level_names = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level_names.append(node.name)
            
            for child in node.children:
                queue.append(child)
        
        results.append(current_level_names)
        
    return results
