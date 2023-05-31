rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total = 0
result = 0
for _ in range(20) :
    s, p, g = input().split()
    p = float(p)
    if g != 'P' :
        total += p
        result += p * grade[rating.index(g)]

print('%.6f' % (result / total))


import sys

data_dict = {"A+": 4.5, "A0": 4.0,
             "B+": 3.5, "B0": 3.0,
             "C+": 2.5, "C0": 2.0,
             "D+": 1.5, "D0": 1.0,
             "F": 0.0}
total = 0
result = 0
for _ in range(0, 20, 1):
    input_data = sys.stdin.readline().split()
    if input_data[2] == "P":
        continue
    total += float(input_data[1])
    result += float(input_data[1]) * data_dict[input_data[2]]
print(result/total)


# GPA = format((result/total), '.6f')
# print(GPA)