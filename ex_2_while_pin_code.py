# DATA LAYER

CLIENT_SECRET_PIN = 1234
CLIENT_FULL_NAME = "John Doe"
CLIENT_BANK_ID = "123abc567xyz"
BANK_NAME = "ING"

# LOGIC & USER INTERFACE
user_pin = 0
pin_try = 0

while pin_try <= 3:
    user_pin = input("PIN: ")
    if len(user_pin) > 4 or len(user_pin) < 4:
        print("INCORRECT PIN. VERIFY YOUR PIN. PLEASE CALL SUPPORT OF " + BANK_NAME)
        quit()
    elif len(user_pin) == 4:
        user_pin = int(user_pin)
    pin_try += 1
    if user_pin == CLIENT_SECRET_PIN:
        print("WELCOME " + CLIENT_FULL_NAME + ".")
        break;
    elif pin_try == 3:
        print("YOUR CARD IS BLOCKED. PLEASE CALL SUPPORT OF " + BANK_NAME)
        break;
    elif user_pin != CLIENT_SECRET_PIN:
        print("INCORRECT PIN. VERIFY YOUR PIN")
