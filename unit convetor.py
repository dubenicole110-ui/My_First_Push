print("=== Unit Convetor ===")
print("1. USD to ZWG")
print("2. Rands to ZWG")
print("3. Pounds to ZWG")
choice = input("Choose an option (1/2/3):")
amount = float(input("enter amount:"))
# Conversion rates (example value - you can change them)
USD_to_ZWG = 13
Rand_to_ZWG = 0.7
Pound_to_ZWG = 16

if choice == "1":
    print("ZWG", amount * USD_to_ZWG)
elif choice == "2" :
    print("ZWG", amount * Rand_to_ZWG) 
elif choice =="3" :
    print("ZWG", amount * Pound_to_ZWG) 
else:
    print("invalid option")        
