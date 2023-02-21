payrate = 10.0
paycheck = 0
try:
    answer = float(input("How many hours did you work? "))

except:
    print("There was an error")
    # does no go to the else

else:
    paycheck = answer * payrate

print(f"Your paycheck is ${paycheck:,.2f}")
