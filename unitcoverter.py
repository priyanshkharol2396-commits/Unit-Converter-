def read_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Please enter a valid number!")


def converter():
    while True:      # MAIN LOOP
        print("\n===== UNIT CONVERTER =====")
        print("1) Celsius → Fahrenheit")
        print("2) Fahrenheit → Celsius")
        print("3) Kilogram → Gram")
        print("4) Gram → Kilogram")
        print("5) Inch → Centimeter")

        c = input("Enter your choice (1-5): ")

        if c == "1":
            x = read_float("Enter °C: ")
            print("°F =", x * 9/5 + 32)

        elif c == "2":
            x = read_float("Enter °F: ")
            print("°C =", (x - 32) * 5/9)

        elif c == "3":
            x = read_float("Enter kg: ")
            print("g =", x * 1000)

        elif c == "4":
            x = read_float("Enter g: ")
            print("kg =", x / 1000)

        elif c == "5":
            x = read_float("Enter inches: ")
            print("cm =", x * 2.54)

        else:
            print("Invalid choice!")
            continue

        # ASK FOR GOING BACK
        again = input("\nDo you want to convert another unit? (Y/N): ").lower()
        if again != "y":
            print("\nThank you for using the Unit Converter!")
            break

converter()
