# #dictionary 
# customer = {
#     "name":"John Smith",
#     "age": 30,
#     "is_verified":True
# }
# #print(customer.get("nae","Not there"))
# customer["name"] = "jacky"
# print(customer["name"])

# phone = input("Phone no.: ")
# digit_map = {
#     "1":"one",
#     "2":"two",
#     "3":"three",
#     "4":"four",
#     "5":"five"
# }
# output = ""
# for chr in phone:
#     output += digit_map.get(chr, "!!!")
# print(output)
  

#EMOJI CODE
message = input(">")
words = message.split(' ')
emojis = {
    ":)":"😃",
    ":(":"😔",
    ":o":"😯",
    ":/":"😐"
}
output =  ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)