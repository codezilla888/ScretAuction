from replit import clear
import art

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
    else:
        run_auction = False
    clear()
max_bid = -1
max_key = ""
for key in auction_dict:
    if auction_dict[key] > max_bid:
        max_bid = auction_dict[key]
        max_key = key
print(f"The winner is {max_key} with a bid of ${auction_dict[max_key]}")
