# Vacuum Cleaner Agent

def vacuum_cleaner(location, room_A, room_B):

    print("Initial State:")
    print("Room A:", room_A)
    print("Room B:", room_B)
    print("Vacuum is in:", location)
    print()

    while room_A == "Dirty" or room_B == "Dirty":

        if location == "A":
            if room_A == "Dirty":
                print("Vacuum is in A -> Suck")
                room_A = "Clean"
            else:
                print("Room A is Clean -> Move to B")
                location = "B"

        elif location == "B":
            if room_B == "Dirty":
                print("Vacuum is in B -> Suck")
                room_B = "Clean"
            else:
                print("Room B is Clean -> Move to A")
                location = "A"

    print("\nFinal State:")
    print("Room A:", room_A)
    print("Room B:", room_B)
    print("Vacuum is in:", location)
    print("All rooms are clean!")


# Input
location = input("Enter vacuum location (A/B): ").upper()
room_A = input("Enter status of Room A (Clean/Dirty): ").capitalize()
room_B = input("Enter status of Room B (Clean/Dirty): ").capitalize()

vacuum_cleaner(location, room_A, room_B)