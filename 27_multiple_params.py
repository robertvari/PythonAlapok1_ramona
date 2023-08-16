# function definition
def say_hello(name, email, address):
    print(f"Hello {name}")
    print(f"Your email is: {email}")
    print(f"You address is: {address}")

# keyworld param
say_hello(email="csaba@gmail.com", address="Eger", name="Csaba")
say_hello("Csaba", "csaba@gmail.com", "Eger")