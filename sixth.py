# numbers = [1,1,1,4]
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)

numbers = [3,4 ,7,5,9,6]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)