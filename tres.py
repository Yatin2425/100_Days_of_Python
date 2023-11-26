print('''
          |\__
                 /   o\__
                |    ___='
                |    \
                 \    \
                  >    \
                 /      \
                |________|
             __/          \__
            /  //  |++|  \\  \
           |  ||   |/\|  ||   |
           |  ||   |\/|  ||   |
            \  \\  |**|  //  /
          ___|==============|___
         |                      |
         |                      |
         |______________________|
             |   |*|\/|*|   |
             |   |*|/\|*|   |
             |   |*|\/|*| P |
             | 1 |*|/\|*| l |
             | s |*|\/|*| a |
             | t |*|/\|*| c |
             |   |*|\/|*| e |
             |   |*|/\|*|   |
             |   |*|\/|*|   |
             |   |*|/\|*|   |
             |   |*|\/|*|   |
             |   |*|/\|*|   |
 ____________|___|*____*|___|____________
|                                        |
|                                        |
|________________________________________|
      ''')
print("Welcome to Chess Island.")
print("Your mission is to Find the Golden Knight.")

choice = input("You encountered a pawn: Choose your attack - Gun or Sword: ").strip().lower()

if choice == "gun":
    print("You use your gun and defeat the pawn.")
    print("The defeated pawn was guarding a secret map.")
    print("The map leads to the location of the Golden Knight.")
    print("Your quest to find the Golden Knight begins!")

    # Player's choice: Swim or Wait for the boat
    swim_or_wait = input("You arrive at the shore of a river. Do you want to swim across (Swim) or wait for a boat (Wait)? ").strip().lower()

    if swim_or_wait == "swim":
        print("You swim across the river and continue your journey.")
        # Continue the game with more challenges.

    elif swim_or_wait == "wait":
        print("You wait for a boat to arrive.")
        # Continue the game with boat-related challenges.

    else:
        print("Invalid choice. You hesitate and lose precious time. The game is over.")
        # You can add game over logic here.

elif choice == "sword":
    print("You use your sword and defeat the pawn.")
    print("The defeated pawn was guarding a secret map.")
    print("The map leads to the location of the Golden Knight.")
    print("Your quest to find the Golden Knight begins!")

    # Player's choice: Swim or Wait for the boat
    swim_or_wait = input("You arrive at the shore of a river. Do you want to swim across (Swim) or wait for a boat (Wait)? ").strip().lower()

    if swim_or_wait == "swim":
        print("You swim across the river and continue your journey.")
        # Continue the game with more challenges.

    elif swim_or_wait == "wait":
        print("You wait for a boat to arrive.")
        # Continue the game with boat-related challenges.

    else:
        print("Invalid choice. You hesitate and lose precious time. The game is over.")
        # You can add game over logic here.

else:
    print("Invalid choice. The pawn attacks you, and you lose the game.")
    # You can add game over logic here.
