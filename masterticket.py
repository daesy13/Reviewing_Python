TICKET_PRICE = 10

tickets_remaining = 100

SERVICE_CHARGE = 2

# Create the calculate price function
def calculate_price(n):
    return (n * TICKET_PRICE) + SERVICE_CHARGE


# Run this code continuosly until we run out of tickets
while tickets_remaining:

    # Output how many tickets are remaining using the tickets_remaining variable

    print("There are {} tickets remaining".format(tickets_remaining))

    # Gather the user's name and assigned to a new variable

    name = input("What is your name?  ")

    # Prompt the user by name and ask how many ticktes they would like

    num_of_tckts = input("Hi {}, how many tickets do you want?  ".format(name))

    try:
        num_of_tckts = int(num_of_tckts)

        # Raise a ValueError if the request is for more tickets than are available
        if num_of_tckts > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))

    # Expect ValueError to happen and handle it appropriatly...remember to test it out
    except ValueError as e:
        # include the error text in the output
        print("Oh no we run into an issue {}. Please try again!".format(e))

    # Calculate the price (num of ticktes X ticket price) and assigned to a variable
    else:
        total_price = calculate_price(num_of_tckts)

        # Output the price to the screen

        print("the total due is ${}".format(total_price))

        # Prompt user if they want to proceed Y/N
        proceed = input("Do you want to continue? Y/N  ")

        # If they want to proceed
        if proceed.upper() == "Y":
        # print out to the screen "SOLD!" to confirm purchase
        # TODO: gather credit card info and process it
            print("SOLD!")
            # and then decrement the tickets remaining by the number of tickets purchased
            tickets_remaining -= num_of_tckts
        # Otherwise...
        else:
        # thanked them by name
            print("Thank you anyways, {}".format(name))

# Notify the user that the tickets are sold out

print("Sorry tickets are all sold out!!! :(")