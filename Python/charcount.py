sentence = input("Please enter the sentence")

character_list = "abcdefghijklmnopqrstuvwxyz"

for x in character_list:
    print(x, end = "")
    print("-", end = "")
    print(sentence.count(x), end = "")
    print("")