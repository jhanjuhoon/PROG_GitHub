import random
import math

participants = int(input("Enter the number of participants: "))
num_winners = int(input("Enter the number of winners: "))

sheets = math.ceil(participants/8)
prize_per_winner = math.floor(8888/num_winners)

tickets = range(1,participants + 1)
winning_tickets = random.sample(tickets, num_winners)

print(f"Total Participants: {participants}")
print(f"Ticket Sheets Needed: {sheets}")
print(f"Prize Per Winner: {prize_per_winner:,} THB")
print(f"Winning Tickets: {winning_tickets }")