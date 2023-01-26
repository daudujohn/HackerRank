# Enter your code here. Read input from STDIN. Print output to STDOUT
returnDate = input()
dueDate = input()

d1, m1, y1 = returnDate.split(' ')
d2, m2, y2 = dueDate.split(' ')
d1 = int(d1)
d2 = int(d2)
m1 = int(m1)
m2 = int(m2)
y1 = int(y1)
y2 = int(y2)


fine = 0

if y1 > y2:
    fine = 10000
elif (y1 == y2) and (m1 > m2):
    fine = 500 * (m1 - m2)
elif (y1 == y2) and (m1 <= m2) and (d1 > d2):
    fine = 15 * (d1 - d2)
    
print(fine)