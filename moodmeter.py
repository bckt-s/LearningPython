


def react(mood):
    while True:
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