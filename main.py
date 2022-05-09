from replit import clear
import art


def get_max_bid(dictionary: dict):
    max_bid = -1
    max_key = ""
    for key in dictionary:
        if dictionary[key] > max_bid:
            max_bid = dictionary[key]
            max_key = key
    print(f"The winner is {max_key} with a bid of ${dictionary[max_key]}")


print(art.logo)
print("Welcome to the secret auction program.")

run_auction = True
auction_dict = {}
while run_auction:
    name = input("What is your name?:\n")
    auction_dict[name] = int(input("What's your bid?:\n"))
    should_run = input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_run == "yes":
        run_auction = True
        clear()
    else:
        run_auction = False
        get_max_bid(auction_dict)
