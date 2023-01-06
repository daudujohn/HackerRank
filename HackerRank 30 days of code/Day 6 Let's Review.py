# Enter your code here. Read input from STDIN. Print output to STDOUT
no_of_test_cases = int(input())
for j in range(no_of_test_cases):
    input_string = input()
    even_string = ''
    odd_string = ''
    for i in range(len(input_string)):
        if (i % 2 == 0):
            even_string += input_string[i]
        else:
            odd_string += input_string[i]
    print(even_string + ' ' + odd_string)