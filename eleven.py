# def greet_user(First_name, Last_name):
#     print(f'Hi {First_name} {Last_name}!')
#     print("Welcome abroad")
# print("start")
# greet_user("John","Smith")
# print("Finish")


def emoji_conv(message):
    words = message.split(" ")
    emojis = {
        ":)":"😃",
        ":(":"😔"
    }
    output = ""
    for w in words:
        output += emojis.get(w,w) + " "
        return output
message = input(">")
print(emoji_conv(message))
     