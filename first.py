# for x in "Python":
#     print(x)
# for x in ['a','b','c']:
#     print(x)
# for x in range(0,10):
#     print(x)
# names = ["AJames","Mary"]

# for name in names:
#     if name.startswith("J"):
#         print("Found")
        
#         break
# else:
#     print("Not found")
# guess = 0
# answer = 5
# while answer != guess:
#     guess = int(input("Guess: "))
# else:
#     pass

# def increment(parameter_list):
#     pass
# def increment (number: int, by: int = 1) -> tuple:
#     return (number, number + by)
# print(increment(2))

# def multiply(*list):
#     total = 1
#     for bum in list:
#         total *= bum
#     return total

# print(multiply(2,3,4,6))

# def save_user(**user):
#     print(user)
# save_user(id=1,name='admin')

def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "fizzbuzz"
    if input % 3 == 0:
        return("fizz")
    if input % 5 == 0:
        return "buzz"
    

    return input

print(fizz_buzz(7))
