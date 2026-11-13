def calculate_change (paid,price):
    change = paid - price 
    return change 

ticket_price = 30

print ("=====PARKING TICKET PAYMENT HELPER=====")
print ("\nThe price of the parking ticket is ", ticket_price,"units" )
print ("\nCoins accepted are:")
print ("1, 5, 10, or 25 ")

total_inserted = 0
coins_inserted = 0

while True:
    coin = int(input("Insert a coin of 1, 5, 10, or 25 : "))

    if coin != 1 and coin != 5 and coin !=10 and coin !=25:
        print ("Invalid coin. Try again with coins accepted!")
        continue

    total_inserted+=coin
    coins_inserted+=1

    print ("\nInserted amount so far :", total_inserted)
    print ("Inserted coins so far :", coins_inserted)    
    print ()
    
    if total_inserted>=ticket_price:
        print ("Enough money inserted!")
        break

change_due = calculate_change(total_inserted,ticket_price)

print ("Thank you for your patience.")
print ("Printing your parking ticket.....")

if change_due==0:
    pass

else:
    print (f"Here is your change : {change_due} units ")

print ("\n=====PAYMENT SUMMARY=====")
print ("\nTicket price : ", ticket_price)
print ("Coins inserted : ",coins_inserted)
print ("Total paid : ", total_inserted)
print ("Change Given : ", change_due)
print ("\n=========================")

print ("THANK YOU!! Have a nice day!")
print ("Parking payment ticket payment complete!")
