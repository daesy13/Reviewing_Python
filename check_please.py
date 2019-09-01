import math

def split_check(total, num_of_people):
    # cost_per_person = math.ceil(total / num_of_people)
    # return cost_per_person
    return math.ceil(total / num_of_people)

# amount_due = split_check(84.97, 4)

total_due = float(input("What is the total?  "))
num_of_people = int(input("How many people?  "))

amount_due=split_check(total_due, num_of_people)

print("Each person owes ${}".format(amount_due))

# Keep in mind that a user can input zero as num
# of people or "four of us"
