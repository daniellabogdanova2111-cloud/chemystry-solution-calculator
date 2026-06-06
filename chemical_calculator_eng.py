print("Solution Mass Fraction Calculator.")
start = input("Run the program? (y/n): ")
while start == "y" or start == "Y":
    print("Program started…")
    print("Choose an action:")
    print("1 — Find mass fraction.")
    print("2 — Find mass of solute.")
    print("3 — Find mass of solution.")
    x = input("1/2/3: ")
    print()

    if x == "1":
        print("Enter the data.")
        b = input("Mass of solute: \n")
        c = input("Mass of solution: \n")
        b = float(b)
        c = float(c)

        while c <= 0:
            print("Mass of solution cannot be negative or zero!\n")
            c = input("Mass of solution: ")
            c = float(c)
        while b <= 0:
            print("Mass of solute cannot be negative or zero!")
            b = input("Mass of solute: ")
            b = float(b)

        mass_fraction = (b / c) * 100
        print(f"Mass fraction: {mass_fraction:.2f}%")
        if mass_fraction > 100:
            print("Mass fraction exceeds 100%, which is impossible. Check your calculations.")
        print()

    elif x == "2":
        print("Enter the data.")
        a = input("Mass fraction of solute (%): \n")
        c = input("Mass of solution: \n")
        a = float(a)
        c = float(c)

        while c <= 0:
            print("Mass of solution cannot be negative or zero!\n")
            c = input("Mass of solution: ")
            c = float(c)
        while a <= 0 or a > 100:
            print("Mass fraction cannot be negative, zero, or exceed 100%!\n")
            a = input("Mass fraction (%): ")
            a = float(a)

        print(f"Mass of solute: {(a * c) / 100:.2f} grams")
        print()

    elif x == "3":
        print("Enter the data.")
        b = input("Mass of solute: \n")
        a = input("Mass fraction of solute (%): \n")
        b = float(b)
        a = float(a)

        while a <= 0 or a > 100:
            print("Mass fraction cannot be negative, zero, or exceed 100%!\n")
            a = input("Mass fraction (%): ")
            a = float(a)
        while b <= 0:
            print("Mass of solute cannot be negative or zero!\n")
            b = input("Mass of solute: \n")
            b = float(b)

        print(f"Mass of solution: {(b / a) * 100:.2f} grams")
        print()

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        x = input("1/2/3: ")
        print()

    start = input("Do you want to continue? (y/n): ")
    print("=========================================")

print("Program terminated.")