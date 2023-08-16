# function definition
def say_hello(name, email=None, address=None):
    print(f"Hello {name}")

    if email:
        print(f"Your email is: {email}")
    
    if address:
        print(f"You address is: {address}")

say_hello("Ákos")