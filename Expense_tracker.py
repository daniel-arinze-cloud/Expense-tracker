budget=int(input("What is your budget? "))
item1=input("What did you buy? ")
price1=int(input("how much? "))
item2=input("What else did you buy? ")
price2=int(input("how much? "))       
item3=input("What else did you buy? ")
price3=int(input("How much? "))
total=price1 + price2 + price3
print(f"You spent {total} today ")
#New - budget check
if total > budget :
	print("Warning: you spent too much! ")
else:
	print("Good job,you stayed within budget! ")