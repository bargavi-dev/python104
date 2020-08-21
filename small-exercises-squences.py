list_of_num = [1, 2, 3, 4, 5]




#sum the numbers
print(sum(list_of_num))

print()
print()

#largest number
print(max(list_of_num))

print()
print()

#smallest number
print(min(list_of_num))

print()
print()

#positive numbers
for num in list_of_num:
    if num >= 0:
        print(num)

print()
print()

#positive numbers II
second_list_of_num = [6, 7, 8, 9, 10]
postive_num_list = []
for num in second_list_of_num:
    if num >= 0:
        postive_num_list.append(num)
print(postive_num_list)

print()
print()

#multiply a list
#list_of_num = [1, 2, 3, 4, 5]

factor = 2

new_multiplied_list = []

for num in list_of_num:
    new_multiplied_list.append(num * factor)
print(new_multiplied_list)


print()
print()

#reverse a string
given_string = input('Give a word: ')
print(given_string[::-1])
