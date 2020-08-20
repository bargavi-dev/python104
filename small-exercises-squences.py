list_of_num = [1, 2, 3, 4, 5]




#sum the numbers
print(sum(list_of_num))

print()

#largest number
print(max(list_of_num))

print()

#smallest number
print(min(list_of_num))

print()

#positive numbers
for num in list_of_num:
    if num >= 0:
        print(num)

print()

#positive numbers II
second_list_of_num = [6, 7, 8, 9, 10]
for num in second_list_of_num:
    if num >= 0:
        print(num)

print()

#multiply a list
#list_of_num = [1, 2, 3, 4, 5]

factor = 2
for num in list_of_num:
    print(factor * num)

print()

#reverse a string
given_string = input('Give a word: ')
print(given_string[::-1])
