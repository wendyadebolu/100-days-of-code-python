from art import logo
print(logo)


def find_highest_bid(bids):
    winner = ''
    highest_bid = 0
    for item in bids:
        bid_amount = bids[item]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = item

    print(f"The winner is {winner} with a bid of ${highest_bid}.")


bids = {}

continue_bidding = True
while continue_bidding:
    name = input("What is your name?: \n")
    bid_price = int(input("What is your bid price?: £\n"))
    bids[name] = bid_price
    should_continue = input("Are there other users who want to bid, type 'yes' or 'no' \n").lower()

    if should_continue == 'no':
        continue_bidding = False
        find_highest_bid(bids)
    elif should_continue == 'yes':
        print("\n" * 50)



