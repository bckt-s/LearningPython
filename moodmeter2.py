def evaluate_mood(user):
    
    prompt = "How are you doing today? "    # Ask user how they are that day.
    
    messages = {    # Save responses for if they reply that they are doing good or bad.
        "good": f"Amazing! It's good to hear that {user}.",
        "bad":  f"Sorry to hear, {user}. Hopefully tomorrow is much better!"
    }
    
    while True:     # Loop using saved responses from above depending on if they say good or bad.
        mood = input(prompt).strip().lower()
        if mood in messages:
            print(messages[mood])
            return mood
        else:
            if prompt.startswith("How are you doing today? "):
                prompt = f"Alright {user}, would you say that's more good or bad? " # Exception handling to force them to say 'good' or 'bad' if they said something prior.
                continue
            else:
                print(f"Well {user}, I hope things are good now and/or in the near future!")
                return mood

def get_name():     # Get name to make responses more personal.
    name = input("Hello! What's your name? ")
    return name


def main():
    user = get_name() # Personal way to say hello.
    print(f"Nice to meet you {user}.") 
    mood = evaluate_mood(user) # Use mood input from user to dictate next response.
    
    if mood == "good":      # Ask to give quote if user is doing good.
        answer = input("Would you like a motivational quote? (yes/no) ").strip().lower()
        if answer == "yes":
            print("'It is not death that a man should fear, but he should fear never beginning to live.' - Marcus Aurelius. ")
        else:
            print("No problem, have a great day!")

    elif mood == "bad": # Ask to give quick tip to user if their day is bad.
        answer = input("Can I share a quick tip to lift your spirits? (yes/no) ").strip().lower()
        if answer == "yes":
            print("You are stronger than you think, you are loved, and tomorrow is a new day!")
        else:
            print("No problem, have a great day!")


if __name__ == "__main__": # Run it all
    main()