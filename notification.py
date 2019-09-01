praise = "you are doing great"
praise = praise.upper() #re assign b/c string are inmutable
number_of_characters = len(praise)
result = praise + "!" * (number_of_characters // 2)
print(result)

advice = "Don't forget to ask for help"
advice = advice.upper()
number_of_characters = len(advice)
result = advice + "!" * number_of_characters
print(result)

advice2 = "Don't Repeat Yourself. Keep things DRY"
advice2 = advice2.upper()
number_of_characters = len(advice2)
result = advice2 + "!" * number_of_characters
print(result)

# Line 4 We were able to change it but it is too
# much work to change all of them, we need to
# create a function

def yell(text):
    text = text.upper()
    number_of_characters = len(text)
    result = text + "!" * (number_of_characters // 4)
    # change the division from 2 to 4
    print(result)

yell("you are doing great")
yell("Don't forget to ask for help")
yell("Don't Repeat Yourself. Keep things DRY")