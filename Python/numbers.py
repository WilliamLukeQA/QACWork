number = int(input("Enter a number between 1-9999 "))

ones_list = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
teens_list = {1: "ten", 2: "eleven", 3: "twelve", 4: "thirteen", 5: "fourteen", 6: "fifthteen", 7: "sixteen", 8: "seventeen", 9: "eigthteen", 10: "nineteen"}
decades_list = {1: "twenty", 2: "thirty", 3: "forty", 4: "fifty", 5: "sixty", 6: "seventy", 7: "eighty", 8: "ninety"}


if (int(number / 1000)) > 0:
    print(ones_list[int(number/1000)] + " thousand")
    number = number % 1000

if (int(number / 100)) > 0:
    print(ones_list[int(number/100)] + " hundred")
    number = number % 100

if (int(number / 10)) > 0:
    print(decades_list[int(number/10) - 1])
    number = number % 10

if (int(number)) > 0:
    print(ones_list[int(number)])

