# I've made a function that creates brand new product names using "artificial intelligence".
# I have a problem though, people keep on adding product ideas that are too short. It makes the suggestions look bad.
# Can you please raise a ValueError if the product_idea is less than 3 characters long? product_idea is a string. Thanks in advance!

def suggest(product_idea):
    if len(product_idea) < 3:
        raise ValueError("...")
    return product_idea + "inator"


