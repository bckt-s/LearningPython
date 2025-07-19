## A mood meter. The large comment is the first set of code with no aid. The second bit was created with little aid/guidance.

## def main():
##   response = input("How are you? ").strip().lower()

##    if response == "good":
##        print("I'm glad, that's good to hear.")
##    elif response == "bad":
##        print("I hope tomorrow is better!")
##    else:
##        question = input("Would you say that's good or bad? ").strip().lower()
##        if question == "good":
##            print("Awesome! I'm glad!")
##        elif question == "bad":
##            print("Hopefully tomorrow is better.")
##        else:
##            print("Hm, not sure what that means, but hopefully all is well!")

##main()


def react(mood):
    if mood == "good":
        print("I'm glad, that's good to hear.")
        return True
    elif mood == "bad":
        print("I hope tomorrow is better!")
        return True
    else:
        return False

def main():
    response = input("How are you? ").strip().lower()
    if not react(response):
        question = input("Would you say that's good or bad? ").strip().lower()
        react(question)

if __name__ == "__main__":
    main()