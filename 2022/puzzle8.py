# %%
import numpy

matrix = []
with open('./2022/input_puzzle_8.txt', 'r') as fp:
    lines = fp.readlines()
    for line in lines:
        line = line.strip()
        row = [int(x) for x in list(line)]
        matrix.append(row)

np_matrix = numpy.asarray(matrix)
print(np_matrix)

# %%
sum_visible = 0
for i in range(len(np_matrix)):
    for j in range(len(np_matrix[i])):
        current_element = np_matrix[i, j]
        row = np_matrix[i, :]
        column = np_matrix[:, j]
        if i == 0 or j == 0 or i == (len(np_matrix) - 1) or j == (len(np_matrix[i]) - 1):
            sum_visible += 1
        else:
            if (
                numpy.all(row[:j] < current_element) or
                numpy.all(row[j+1:] < current_element) or
                numpy.all(column[:i] < current_element) or
                numpy.all(column[i + 1:] < current_element)
            ):
                sum_visible += 1
print(sum_visible)

# %%
scenic_score = 0
for i in range(len(np_matrix)):
    for j in range(len(np_matrix[i])):
        current_element = np_matrix[i, j]
        west = np_matrix[i, :j]
        west_score = 0
        east = np_matrix[i, j+1:]
        east_score = 0
        north = np_matrix[:i, j]
        north_score = 0
        south = np_matrix[i+1:, j]
        south_score = 0
        for w in range(len(west) - 1, -1, -1):
            if west[w] < current_element:
                west_score += 1
            else:
                west_score += 1
                break
        for e in range(len(east)):
            if east[e] < current_element:
                east_score += 1
            else:
                east_score += 1
                break
        for n in range(len(north) - 1, -1, -1):
            if north[n] < current_element:
                north_score += 1
            else:
                north_score += 1
                break
        for s in range(len(south)):
            if south[s] < current_element:
                south_score += 1
            else:
                south_score += 1
                break
        if west_score * east_score * north_score * south_score > scenic_score:
            scenic_score = west_score * east_score * north_score * south_score

print(scenic_score)
