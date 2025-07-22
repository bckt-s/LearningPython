
def main(): # Get int for x and have defense/alert if something else is typed.
    x = get_int()
    print(f"x is {x}.")

def get_int():
    while True: # Loop until integer is provided.
        try:
            return int(input("What's x? ")) # Ask for int and RETURN it.
        except ValueError:
            print("x is not an integer.") # Alert if they provide str.

main()