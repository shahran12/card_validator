


def credit_card_validation(credit_number):
	
	card_number=[]
	card_number = input("Enter Credit Card credit_number")
	card_number_final = list(map(int,card_number))
	if len(card_number) != 15 or len(card_number) != 16:
		print ("Wrong Card number")


def card_type(card_number):
	if card_number[:4] in  ["6011"]: 
		card_type = "Discover"
	elif card_number[:2] in ["51", "52", "53", "54", "55"]:
		card_type = "Mastercard"
	elif card_number[:2] in ["34", "37"]: 
		card_type = "AMEX"
	elif card_number[0] in ["4"]:
		card_type = "Visa"
	else:
		card_type = 'INVALID'
	return card_type

card_number_final1 = [5,5,1,5,4,6,0,9,3,4,3,6,5,3,1,6]	

def verification(card_number_final1):
	khh = [i*2 for i in card_number_final1[-1::-2]]
	print (khh)

	numCC = [num if num < 10 else 1 + num % 10 for num in khh]
	print (numCC)

	total = sum(numCC) + sum(card_number_final1)
    
	if  total % 10 == 0:
		print ("Card  Validated Congratulations !!!!")

	else:
		print ("Invalid card number")

 



verification(card_number_final1)