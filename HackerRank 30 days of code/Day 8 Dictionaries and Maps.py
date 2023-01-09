# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phoneBook = {}
for i in range(n):
    friend = input()
    phoneBook[friend.split(' ')[0]] = friend.split(' ')[1]
for i in range(n):
    name = input()
    if name in phoneBook:
        print(f'{name}={phoneBook[name]}')
    else:
        print('Not found')