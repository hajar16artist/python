# Smart Grid Appliance Energy Calculator

devices = {
    1: {"name": "AC", "wattage": 1300},
    2: {"name": "Lights", "wattage": 100},
    3: {"name": "Fridge", "wattage": 300}
}


def calculate_kwh(wattage, hours):
    return (wattage * hours) / 1000


print("HOME SYSTEMS")
print("============")
print("Choose from: devices / done")

while True:

    choice = input("\nChoose a system: ").lower()

    if choice == "done":
        break

    if choice == "devices":

        print("\nDEVICES")
        print("1 - AC")
        print("2 - Lights")
        print("3 - Fridge")

        device_choice = int(input("Choose from 1 to 3: "))

        if device_choice in devices:

            device = devices[device_choice]

            print("\nDevice:", device["name"])
            print("Wattage:", device["wattage"], "W")

            hours = float(input("Enter usage hours: "))

            energy = calculate_kwh(
                device["wattage"],
                hours
            )

            print("Energy used:", round(energy, 2), "kWh")

            continue_choice = input(
                "Do you want to continue? (yes/done): "
            ).lower()

            if continue_choice == "done":
                break

        else:
            print("Please choose a number from 1 to 3.")

    else:
        print("Please choose devices or done.")


print("\nProgram finished.")