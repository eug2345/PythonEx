deposit = 10

if 0 < deposit <= 100:
    print(f"Thank you for the £{deposit} deposit!")
else:
    print("This is not a valid amount to deposit.")

    deposit = 10
password = "password"

if 0 < deposit <= 100 and password == "password":
    print(f"Thank you for depositing £{deposit}!")
else:
    print("Failed to make a deposit.")

    deposit = 10
password = "password"

if not (0 < deposit <= 100) or password != "password":
    print("Failed to make a deposit.")
else:
    print(f"Thank you for depositing £{deposit}!")

    name = "Ollie"

if name in ("root", "admin"):
    print("This is not a valid username!")
else:
    print(f"Welcome, {name}!")

    name = "Ollie"

if name not in ("root", "admin"):
    print(f"Welcome, {name}!")
else:
    print("This is not a valid username!")

    age = int(input("Enter your age: "))

if age >= 85:
    print("You are above 85")
elif age >= 50:
    print("You are between 50 and 85")
elif age >= 20:
    print("You are between 20 and 50")
else:
    print("You are below 20 years old")