# Odd versus even
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


# The most succint
def is_even(n):
    return n % 2 == 0

    
main()