# numbers = [5,6,8,5,3]
# numbers2 = numbers.copy()
# numbers2.reverse()
# print(numbers)
# print(numbers2)

numbers = [2,2,4,4,5,5,7,8,9,7,8]
uniq = []
for number in numbers:
    if number not in uniq:
        uniq.append(number)
print(uniq)