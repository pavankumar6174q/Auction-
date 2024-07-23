#SECRET AUCTION

#This is an auction 
bids = {}  #created an empty dictionary to add all the input bids

not_end = True   # taking a condition so that we can use while loop 

def find_highest_bidder(bidderz):  # The function to find highest bidder 
    highest = 0  #assigning the highest value to 0
    for bidder in bids:             #looping through the bids
        bid_value = bidderz[bidder]# here we are taking the keys from the bids and assigning their values to bid_value
        if bid_value > highest:   # we are comparing the values with the bid values 
            
            highest = bid_value #then changing the highest value according to that
    print(f'The highest bid is {highest}, the bidder won is {bidder}')


while not_end:
    name = input("enter name:  ") #taking input from users
    amount = int(input("enter amount:  "))  #taking input from users
    bids[name] = amount  #assigning the input values as keys and its values in the dictionary named bids
    should_continue = input("enter y or n : ").lower()  #if the user wants to continue or not
    
    if should_continue == "n":
        find_highest_bidder(bids) #calling the above function
        not_end = False #ending the while loop

