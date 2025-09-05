from auction_art import logo

print(logo)

def find_the_highest(top_bid):
    highest = 0
    winner = ""
    for bidder in top_bid:
        bid_amount = top_bid[bidder]
        if bid_amount > highest:
            highest = bid_amount
            winner = bidder
    print(f"The winner is {winner} with bid ${highest}")

bids = {}
should_continue =True
while should_continue:
    name = input("Enter you name: ")
    price = int(input("Enter the bid amount: $"))
    bids[name] = price
    choice = input("if there are any other bidders type 'YES' or if not type 'NO'").upper()
    if choice =="NO":
        should_continue = False
        find_the_highest(bids)
    if choice =="YES":
        print("\n"*20)




