A_list = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
B_list = [4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.0]
sum = 0
total = 0
for _ in range(20):
    subject, credit, grade = input().split()
    if grade != 'P':
        total += float(credit) * B_list[A_list.index(grade)]
        sum += float(credit)
print(total/sum)

