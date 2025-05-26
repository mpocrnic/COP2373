# This program sells a limited number of cinema tickets.
# Each person can purchase up to 4 tickets.
# The program prompts for ticket purchases until all 20 tickets are sold.
# After that, it displays the total number of buyers.


# Constants defining the max number of tickets available overall
# and the maximum a person can buy
MAX_TICKETS = 20
MAX_PER_PERSON = 4

# This is a function to process the number of tickets requested
def getTickets(wanted, remaining):
    
    # If someone wants less than 1 ticket, it's invalid
    if wanted < 1:
        print("You need to buy at least one ticket.")
        return 0
    
    # If someone wants more than the max allowed per person, it's invalid
    elif wanted > MAX_PER_PERSON:
        print(f"You can only buy up to {MAX_PER_PERSON} tickets.")
        return 0
    
    # If someone wants more tickets than are left, it's invalid
    elif wanted > remaining:
        print("Not enough tickets left.")
        return 0
    
    # If all the conditions are satisfied return the number of tickets they can buy
    else:
        return wanted
    
# This is the main function to control how the ticket selling works
def main():
    ticketsLeft = MAX_TICKETS
    totalBuyers = 0

    print("Welcome to the Cinema Ticket Sale")

    # Loop until no tickets are left
    while ticketsLeft > 0:

        # This is to show  how many tickets are still available
        print(f"\nTickets remaining: {ticketsLeft}")

        try:

            # Ask person how many tickets they want
            wantedTickets = int(input("How many tickets do you want? "))

            # Call the function to validate the ticket request
            bought = getTickets(wantedTickets, ticketsLeft)

            if bought > 0:
                ticketsLeft -= bought
                totalBuyers += 1
                print(f"You bought {bought} ticket(s). {ticketsLeft} left.")

        except ValueError:
            print("Please enter a valid number.")
    # After the loop ends all tickets are sold
    print(f"\nAll tickets sold. Total buyers: {totalBuyers}")

main()
