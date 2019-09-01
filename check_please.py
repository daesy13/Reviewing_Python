import math

def split_check(total, num_of_people):
    # cost_per_person = math.ceil(total / num_of_people)
    # return cost_per_person
    if  num_of_people <= 1:
        raise ValueError("More than one person is required to split the check")
    return math.ceil(total / num_of_people)

# amount_due = split_check(84.97, 4)

try:
    total_due = float(input("What is the total?  "))
    num_of_people = int(input("How many people?  "))
    amount_due=split_check(total_due, num_of_people)
except ValueError as err:
    print("Oh no! That is not a valid value. Try again...")
    print("({})".format(err))
# except ZeroDivisionError:
#     print("Oh no! That is not a valid value. Try again...")
else:

    print("Each person owes ${}".format(amount_due))
# finally:
#     pass





# Keep in mind that a user can input zero as num
# of people or "four of us"
# Also try with negative numbers for "How many ppl"

