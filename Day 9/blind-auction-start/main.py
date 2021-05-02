from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")
continue_bid = True
bidders = []
while continue_bid:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    # Store names and bids into dictionary then into list
    bidder = {}
    bidder["name"] = name
    bidder["bid"] = bid
    bidders.append(bidder)

    more_bidder = input ("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more_bidder == "no":
        continue_bid = False
    elif more_bidder == "yes":  
        clear()

def find_bid_winner(bidders_list):
    highest_bid = 0
    winner = ""
    for bidder_dict in bidders_list:
        if bidder_dict["bid"] > highest_bid:
            winner = bidder_dict["name"]
            highest_bid = bidder_dict["bid"]

    print(f"The winner is {winner} with a bid of ${highest_bid}")

find_bid_winner(bidders)