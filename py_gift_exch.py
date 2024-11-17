"""Christmas Gift Exchange."""
# JDD 11/2024

import random

def main():
    """main is the Main."""
    print("\nWelcome to the PyGift Exchange Name Generator!")

    # List of people participating in the gift exchange
    participants = ["Jeff", "Larry", "Angi", "Holli", "Brad", "Darin", "Amy", "Julie"]

    # Shuffle the participants to create a randomized giving and receiving pair
    givers = participants[:]
    receivers = participants[:]

    # Ensure no one receives their own gift and no giver receives from the person they are giving to
    valid = False
    while not valid:
        random.shuffle(receivers)
        random.shuffle(givers)
        valid = all(
            giver != receiver and receivers[(i + 1) % len(receivers)] != giver
            for i, (giver, receiver) in enumerate(zip(givers, receivers))
        )

    # Print the gift exchange list
    print("Christmas Gift Exchange Pairs:\n")
    for giver, receiver in zip(givers, receivers):
        print(f"{giver} gives a gift to {receiver}\n")

# main

if __name__ == "__main__":
    main()

# end
