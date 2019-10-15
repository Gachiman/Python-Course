import re

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []
for _ in range(n):
    matrix.append(input())

string = ""
for i in range(m):
    for j in range(n):
        string += matrix[j][i]

print(re.sub(r'(?<=[0-9a-zA-Z])[!@#$%& ]+(?=[0-9a-zA-Z])', ' ', string))
