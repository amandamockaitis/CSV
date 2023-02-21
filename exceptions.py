payrate = 10.0
paycheck = 0

while True:
    try:
        answer = float(input("How many hours did you work? "))
        paycheck = answer * payrate
        print(f"Your paycheck is ${paycheck:,.2f}")
        break

    except ValueError as err:
        print(f"There was an error. The error code is: {err}")
        # does no go to the else

print("It is done")
