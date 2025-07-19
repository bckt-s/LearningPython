# Say hello to user and use their name.

def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="there..."):
    print("Hello,", to)

hello()
main()