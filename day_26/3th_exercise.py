file1_numbers = []
file2_numbers = []
with open("file1.txt") as file1:
    file1_numbers = [n.replace("\n", "") for n in file1.readlines()]

with open("file2.txt") as file2:
    file2_numbers = [n.replace("\n", "") for n in file2]

result = [int(n) for n in file1_numbers if n in file2_numbers]

print(result)

