number = int(input("Enter a number between 1-9999"))

ones_list = {1: "zero", 2: "one", 3: "two", 4: "three", 5: "four", 6: "five", 7: "six", 8: "seven", 9: "eight", 10: "nine"}
teens_list = {1: "ten", 2: "eleven", 3: "twelve", 4: "thirteen", 5: "fourteen", 6: "fifthteen", 7: "sixteen", 8: "seventeen", 9: "eigthteen", 10: "nineteen"}
decades_list = {1: "twenty", 2: "thirty", 3: "forty", 4: "fifty", 5: "sixty", 6: "seventy", 7: "eighty", 8: "ninety"}
hundred_list = {1: "one hundred", 2: "two hundred", 3: "three hundred", 4: "four hundred", 5: "five hundred", 6: "six hundred", 7: "seven hundred", 8: "eight hundred", 9: "nine hundred"}
thousand_list = {1: "one thousand", 2: "two thousand", 3: "three thousand", 4: "four thousand", 5: "five thousand", 6: "six thousand", 7: "seven thousand", 8: "eight thousand", 9: "nine thousand"}

if number < 9:
    print(ones_list[number + 1])
if number > 9 and number < 19:
    print(teens_list[number - 9])
if number > 19 and number < 99:
    number.length

