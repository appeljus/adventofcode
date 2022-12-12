# %%
import numpy as np
import string
import scipy

alphabet_list = list(string.ascii_lowercase)


def check_traversable(node1, node2) -> bool:
    if node1 == "S":
        node1 = "a"
    if node1 == "E":
        node1 = "z"
    if node2 == "S":
        node2 = "a"
    if node2 == "E":
        node2 = "z"
    if node1 == node2:
        return True
    elif node1 == 'a':
        if node2 == 'b':
            return True
        else:
            return False
    else:
        if (
            alphabet_list.index(node1) > alphabet_list.index(node2) or
            alphabet_list[alphabet_list.index(node1) + 1] == node2
        ):
            return True
        else:
            return False


def parse_input():
    matrix = []
    with open('./2022/input_puzzle_12.txt', 'r') as fp:
        for line in fp:
            matrix.append(list(line.strip()))
    graph_matrix = np.zeros(
        (
            len(matrix) * len(matrix[0]),
            len(matrix) * len(matrix[0])
        )
    )
    y_length = len(matrix[0])
    start_node_id = 0
    end_node_id = 0
    for x in range(len(matrix)):
        for y in range(y_length):
            current_node = matrix[x][y]
            current_node_id = x * y_length + y
            if current_node == "S":
                start_node_id = current_node_id
            if current_node == "E":
                end_node_id = current_node_id
            if x != 0:
                up_node = matrix[x - 1][y]
                up_node_id = (x - 1) * y_length + y
                if check_traversable(current_node, up_node):
                    graph_matrix[current_node_id, up_node_id] = 1
            if x != len(matrix) - 1:
                down_node = matrix[x + 1][y]
                down_node_id = (x + 1) * y_length + y
                if check_traversable(current_node, down_node):
                    graph_matrix[current_node_id, down_node_id] = 1
            if y != 0:
                left_node = matrix[x][y - 1]
                left_node_id = x * y_length + y - 1
                if check_traversable(current_node, left_node):
                    graph_matrix[current_node_id, left_node_id] = 1
            if y != y_length - 1:
                right_node = matrix[x][y + 1]
                right_node_id = x * y_length + y + 1
                if check_traversable(current_node, right_node):
                    graph_matrix[current_node_id, right_node_id] = 1
    return graph_matrix, start_node_id, end_node_id, matrix


# %%
# Part 1
graph, start_node, end_node, _ = parse_input()
dist_matrix = scipy.sparse.csgraph.shortest_path(graph, directed=True, unweighted=True)
print(dist_matrix[start_node, end_node])

# %%
# Part 2
graph, _, end_node, matrix = parse_input()
dist_matrix = scipy.sparse.csgraph.shortest_path(graph, directed=True, unweighted=True)
fewest_step = 394
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "a":
            if dist_matrix[i * len(matrix[i]) + j, end_node] < fewest_step:
                fewest_step = dist_matrix[i * len(matrix[i]) + j, end_node]
print(fewest_step)

