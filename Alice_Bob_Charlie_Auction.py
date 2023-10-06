 # Alice, Bob and Charlie are bidding on an artifact at an auction.
# Alice bids A rupees, Bob bids B rupees and Charlie bids C rupees (where A, B and C are distinct).
# According to the rule of the auction, the one who bids the highest amount will win the auction. Determine who will win the auction.
# Input:
# Take input of alice, bob and Charlie’s amount.
# Output:
# Print the name of auctioner who wins the auction.

alice_amount = float(input("Enter the alice amount:"))
bob_amount = float(input("Enter the bob amount:"))
charlie_amount = float(input("Enter the charlie amount:"))

if alice_amount > bob_amount and alice_amount > charlie_amount:
    print("Alice won the auction")

elif bob_amount > alice_amount and bob_amount > charlie_amount:
    print("Bob won the auction")

else:
    print("Charlie won the auction")