# %%
from anytree import Node, RenderTree, PreOrderIter, PostOrderIter

with open('input_puzzle_7.txt', 'r') as fh:
    text = fh.read()
    lines = text.split('\n')

root = Node({'dirname': '/'})
parent = root
ls_mode = False
for line in lines:
    if line.startswith('$ cd /'):
        ls_mode = False
        parent = root
    elif line.startswith('$ cd'):
        ls_mode = False
        dirname = line[5:]
        if dirname == '..':
            parent = parent.parent
        else:
            prev_parent = parent
            parent = Node({'dirname': dirname}, parent=prev_parent)
    elif line.startswith('$ ls'):
        ls_mode = True
    elif ls_mode:
        if len(line) > 0 and not line.startswith('dir '):
            (size, name) = line.split()
            new_file = Node({'filename': name, 'size': int(size)}, parent=parent)
    else:
        ls_mode = False
        print("unknown line: ", line)


# %%

def calc_dir_size(node: Node):
    dir_size_sum = 0
    for child in node.children:
        if "filename" in child.name.keys():
            dir_size_sum += child.name["size"]
        elif "dirname" in child.name.keys():
            dir_size_sum += calc_dir_size(child)
        else:
            print("UNKOWN NODE INSTANCE")
    node.name["size"] = dir_size_sum
    return dir_size_sum


# %%
calc_dir_size(root)

# %%
# Part 1
for pre, fill, node in RenderTree(root):
    print(f"{pre} {node.name}")

total_size_dirs = 0
for node in PreOrderIter(root):
    if "dirname" in node.name.keys():
        if node.name["size"] <= 100000:
            total_size_dirs += node.name["size"]
print(total_size_dirs)

# %%
# Part 2
in_use = root.name["size"]
free_space = 70000000 - in_use
size_to_delete = 30000000 - free_space
smallest_dir_size = in_use
for node in PreOrderIter(root):
    if "dirname" in node.name.keys():
        if node.name["size"] >= size_to_delete:
            if node.name["size"] < smallest_dir_size:
                smallest_dir_size = node.name["size"]
print(smallest_dir_size)
