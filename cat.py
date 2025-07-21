# Practice with loops

# meow 9 times

# for _ in range(3): # Not using variable in the future
#     print("meow\n" * 3, end="") # overcomplicated but testing features


def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("How many meows? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()