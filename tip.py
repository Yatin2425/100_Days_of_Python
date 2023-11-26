a = float(input("What was the total bill? $ "))
b = int(input("What tip percentage would you like to give? 10, 12, 15 "))
c = int(input("How many people to split the bill? "))

# Calculate the bill per person
bill_per_person = (a + (b / 100 * a)) / c

# Print the bill per person with two decimal places
print(f"Each person should pay: ${bill_per_person: .2f}")
