def calculate_momentum():
    try:
        mass = float(input("Enter the mass of the object (in kilograms): "))
        velocity = float(input("Enter the velocity of the object (in meters per second): "))
        momentum = mass * velocity

        print(f"\nThe momentum of the object is: {momentum} kg·m/s")

    except ValueError:
        print("Invalid input. Please enter numeric values for mass and velocity.")
calculate_momentum()
